from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import data_required


class AddDrinker(FlaskForm):
    name = StringField('Name', validators=[data_required()])
    age = IntegerField('Age', validators=[data_required()])
    country = StringField('Country', default=None)
    submit = SubmitField('Add a New Drinker')
