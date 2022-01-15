from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField, SelectMultipleField, SelectField
from wtforms.validators import data_required, NumberRange


class Login(FlaskForm):
    age = IntegerField('Age', validators=[data_required(), NumberRange(min=18)])
    submit = SubmitField('Submit')


class AddDrinker(FlaskForm):
    name = StringField('Name', validators=[data_required()])
    age = IntegerField('Age', validators=[data_required(), NumberRange(min=18)])
    country = StringField('Country', default=None)
    gender = RadioField('Gender', choices=['M', 'F'])
    submit = SubmitField('Add a New Drinker')


class AddDrink(FlaskForm):
    distillery = StringField('Distillery', validators=[data_required()])
    edition = StringField('Edition', validators=[data_required()])
    color = StringField('Color', default=None)
    nose = SelectField('Nose',
                               choices=[("Elegant & Floral", "Elegant & Floral"), ("Fresh Fruit & Vanilla", "Fresh Fruit & Vanilla"), ("Dried Fruit & Nut", "Dried Fruit & Nut"),
                                        ("Malt & Honey", "Malt & Honey"), ("Rich Fruit & Spice", "Rich Fruit & Spice"), ("Peat & Fruit", "Peat & Fruit"),
                                        ("Maritime & Smoky", "Maritime & Smoky"), ("Rich & Peaty", "Rich & Peaty")], default=None)
    palate = SelectField('Palate',
                                 choices=[("Elegant & Floral", "Elegant & Floral"), ("Fresh Fruit & Vanilla", "Fresh Fruit & Vanilla"),
                                          ("Dried Fruit & Nut", "Dried Fruit & Nut"),
                                          ("Malt & Honey", "Malt & Honey"), ("Rich Fruit & Spice", "Rich Fruit & Spice"), ("Peat & Fruit", "Peat & Fruit"),
                                          ("Maritime & Smoky", "Maritime & Smoky"), ("Rich & Peaty", "Rich & Peaty")], default=None)
    finish = SelectField('Finish',
                         choices=[("Very short", "Very short"), ("Short", "Short"), ("Medium", "Medium"), ("Long", "Long"), ("Very long", "Very long")]
                         , default=None)
    submit = SubmitField('Add a New Drink')
