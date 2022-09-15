from flask import Flask, render_template
from form import ValidationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'


@app.route('/', methods=['GET', 'POST'])
def form():
    form = ValidationForm()
    if form.validate_on_submit():
        return render_template('done.html', form=form)
    return render_template('index.html', form=form)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)