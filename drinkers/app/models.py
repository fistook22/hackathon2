from app import db
from sqlalchemy.orm import validates


class Drinker(db.Model):
    drinker_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    country = db.Column(db.String(64))
    gender = db.Column(db.String(2))

    drinks = db.relationship('TheDrink', backref='thedrink', lazy='dynamic')

    # @validates('gender')
    # def validate_gender(self, key, gender):
    #     if gender not in ['M', 'F']:
    #         raise Exception(f'the gender {gender} must be "M" or "F"')


class TheDrink(db.Model):
    drink_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    distillery = db.Column(db.String(64))
    name = db.Column(db.String(64))
    color = db.Column(db.String(32))
    # nose = db.Column(db.List[''])
    # palate = db.Column(db.List[''])
    finish = db.Column(db.String(32))

    person = db.Column(db.Integer, db.ForeignKey('drinker.drinker_id'))
