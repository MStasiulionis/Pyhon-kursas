from flask import Flask, render_template, request
from src.data import data

# iš flask bibliotekos importuojame klasę Flask ir f-ją render_template.
app = Flask(__name__)
# inicijuojame klasės Flask objektą, priskiriame kintamąjam app.


# įvelkame f-ją į flask dekoratorių. Be jo  funkcija būtų bereikšmė. Dekorato riaus parametruose nurodome, kad norėsime
# rezultato 127.0.0.1:8000/ url adrese."""
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        autorius = request.form['autorius']
        tekstas = request.form['tekstas']
        pavadinimas = request.form['pavadinimas']
        data.append({
            'data': date,
            'autorius': autorius,
            'pavadinimas': pavadinimas,
            'tekstas': tekstas,
            'status': 'published'
        })
    return render_template('index.html', data=data)
# funkcijoje index nurodome, kad norėsime sugeneruoti base.html


@app.route('/<string:title>') # parametruose nurodomas kintamasis (title) ir jo tipas (string)
def article(title): # kintam1jį būtinai nurodykite ir funkcijos parametruose
    return render_template('article.html', title=title, data=data) # taip pat ir čia reikia jį perduoti


@app.route('/add_article')
def add_article():
    return render_template('add_article.html')


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

# patikrinę, ar programa leidžiama ne iš kito failo, leidžiame mūsų app, su parametrais. debug = True klaidos atveju
# mums rodys informatyvias žinutes naršyklėje.