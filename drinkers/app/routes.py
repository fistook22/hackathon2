from faker import Faker
from flask import render_template
from app import app, db
from app.models import Drinker


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/notforu', methods=['GET', 'POST'])
def notforu():
    return render_template("notforu.html")


@app.route('/add_fake_drinker', methods=['GET', 'POST'])
def add_drinker():
    faker = Faker()
    name = faker.first_name()
    age = faker.age()
    country = faker.country()

    drinker = Drinker(name=name, age=age, country=country)

    db.session.add(drinker)

    db.session.commit()

    return f"{name} added to the db."


@app.route('/taste', methods=['GET', 'POST'])
def tasting():
    return render_template("whiskywheel.html")


@app.route('/statistics', methods=['GET', 'POST'])
def data_view():
    return render_template("dataview.html")


@app.route('/history', methods=['GET', 'POST'])
def history():
    return render_template("history.html")
