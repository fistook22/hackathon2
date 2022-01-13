from faker import Faker
from flask import render_template
from app import app, db
from app.forms import AddDrinker, AddDrink
from app.models import Drinker


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/notforu', methods=['GET', 'POST'])
def notforu():
    return render_template("notforu.html")


@app.route('/add_drinker', methods=['GET', 'POST'])
def add_drinker(name=None, country=None, age=None, gender=None):
    form = AddDrinker()
    if form.validate_on_submit():
        drinker = Drinker(name=name, age=age, country=country, gender=gender)
        db.session.add(drinker)

        db.session.commit()
        return f'{name} was added to the database'
    return render_template("adddrinker.html", form=form)


@app.route('/taste', methods=['GET', 'POST'])
def tasting():
    form = AddDrink()
    if form.validate_on_submit():
        return render_template("history.html")
    return render_template("whiskywheel.html", form=form)


@app.route('/statistics', methods=['GET', 'POST'])
def data_view():
    return render_template("dataview.html")


@app.route('/history', methods=['GET', 'POST'])
def history():
    return render_template("history.html")
