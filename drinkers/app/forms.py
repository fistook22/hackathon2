from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, RadioField
from wtforms.validators import data_required


class AddDrinker(FlaskForm):
    name = StringField('Name', validators=[data_required()])
    age = IntegerField('Age', validators=[data_required()])
    country = StringField('Country', default=None)
    gender = RadioField('Gender', choices=['M', 'F'])
    submit = SubmitField('Add a New Drinker')


class AddDrink(FlaskForm):
    distillery = StringField('Distillery', validators=[data_required()])
    name = IntegerField('Name', validators=[data_required()])
    color = StringField('Country', default=None)
    nose = StringField('Nose', default=None)
    palate = StringField('Palate', default=None)
    finish = SelectField('Finish', choices=[("Very short", "Short", "Medium", "Long", "Very long")], default=None)
    submit = SubmitField('Add a New Drink')
