from faker import Faker
from flask import render_template, redirect


from app import app, db
from app.forms import AddDrinker, AddDrink, Login
from app.models import Drinker, TheDrink


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/notforu', methods=['GET', 'POST'])
def notforu():
    return render_template("notforu.html")


@app.route('/add_drinker', methods=['GET', 'POST'])
def add_drinker():
    form_drinker = AddDrinker()
    if form_drinker.validate_on_submit():
        name = form_drinker.name.data
        age = form_drinker.age.data
        country = form_drinker.country.data
        gender = form_drinker.gender.data
        drinker = Drinker(name=name, age=age, country=country, gender=gender)

        db.session.add(drinker)

        db.session.commit()

        return redirect("/taste")
    return render_template("adddrinker.html", form=form_drinker)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = Login()
    if form.validate_on_submit():
        return redirect("/add_drinker")
    return render_template("login.html", form=form_login)


@app.route('/taste', methods=['GET', 'POST'])
def tasting():
    form_drink = AddDrink()
    if form_drink.validate_on_submit():
        distillery = form_drink.distillery.data
        edition = form_drink.edition.data
        color = form_drink.color.data
        nose = form_drink.nose.data
        palate = form_drink.palate.data
        finish = form_drink.finish.data

        if edition not in [edition for edition in TheDrink.query.all()]:
            drink = TheDrink(distillery=distillery, edition=edition, color=color, nose=nose, palate=palate, finish=finish)
            db.session.add(drink)
            db.session.commit()

        return redirect("/history")
    return render_template("taste.html", form=form_drink)


@app.route('/statistics', methods=['GET', 'POST'])
def data_view():
    return render_template("dataview.html")


@app.route('/history', methods=['GET', 'POST'])
def history():

    return render_template("history.html")
