import os

from flask import Flask, render_template, request, flash, url_for
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from db import db
from models.User import User
from models.Products import Products
from scr.file_utils import save_picture
from scr.forms.product_form import ProductForm
from scr.forms.login_form import LoginForm
from scr.forms.profile_form import ProfileForm
from scr.forms.registration_form import RegistrationForm
from scr.forms.request_reset_form import RequestResetForm, PasswordResetForm
from flask_mail import Message, Mail
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from password import password

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "testas2.testuotas@gmail.com"
app.config['MAIL_PASSWORD'] = password

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'register'
login_manager.login_message_category = 'info'
login_manager.unauthorized_callback = lambda: render_template("404.html")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@staticmethod
def get_reset_token(user, expires_sec=1800):
    s = Serializer(app.config['SECRET_KEY'], expires_sec)
    return s.dumps({'user_id': user.id}).decode('utf-8')


@staticmethod
def verify_reset_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token)['user_id']
    except:
        return None
    return User.query.get(user_id)


@app.route('/')
def index():
    db.create_all()
    return render_template('index.html')


def send_reset_email(user):
    token = get_reset_token(user)
    msg = Message('Slapta??od??io atnaujinimo u??klausa',
                  sender='testas2.testuotas@gmail.com',
                  recipients=[user.email])
    msg.body = f'''Nor??dami atnaujinti slapta??od??, paspauskite nuorod??:
    {url_for('reset_token', token=token, _external=True)}
    Jei j??s nedar??te ??ios u??klausos, nieko nedarykite ir slapta??odis nebus pakeistas.
    '''
    mail.send(msg)


class ManoModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.username == "My_name"


admin = Admin(app)
admin.add_view(ManoModelView(User, db.session))

mail = Mail(app)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Products(proruct_name=form.product_name.data, product_price=form.product_price.data,
                           amount=form.amount.data)
        db.session.add(product)
        db.session.commit()
        flash('S??kmingai prid??jote prek??!', 'success')
        return render_template('add_success.html', form=form)
    return render_template('add_product.html', form=form)


@app.route('/flash')  # parametruose nurodomas kintamasis (title) ir
def flash_messages():  # kintam1j?? b??tinai nurodykite ir funkcijos parametruose
    flash('S??kmingai prisiregistravote! Galite prisijungti', 'danger')
    return render_template('info.html')  # taip pat ir ??ia reikia j?? perduoti


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data,
                    password=password_hash)
        db.session.add(user)
        db.session.commit()
        flash('S??kmingai prisiregistravote! Galite prisijungti', 'success')
        return redirect(url_for('index'))
    return render_template('registration.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Prisijungti nepavyko. Patikrinkite el. pa??t?? ir slapta??od??', 'danger')
    return render_template('login.html', title='Prisijungti', form=form)


@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        if form.avatar.data:
            avatar = save_picture(app.root_path, form.avatar.data)
            current_user.avatar = avatar
        current_user.username = form.name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Tavo paskyra atnaujinta!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.name.data = current_user.username
        form.email.data = current_user.email
    avatar = url_for('static', filename='avatars/' + current_user.avatar)
    return render_template('profile.html', title='Account', form=form, avatar=avatar)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Jums i??si??stas el. lai??kas su slapta??od??io atnaujinimo instrukcijomis.', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = verify_reset_token(token)
    if user is None:
        flash('U??klausa netinkama arba pasibaigusio galiojimo', 'warning')
        return redirect(url_for('reset_request'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user.password = hashed_password
        db.session.commit()
        flash('Tavo slapta??odis buvo atnaujintas! Gali prisijungti', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)


@app.errorhandler(404)
@app.errorhandler(403)
@app.errorhandler(500)
def error_handler(error):
    return render_template("404.html", error=error)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
