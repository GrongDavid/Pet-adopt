from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Length, URL, Optional

class AddPetForm(FlaskForm):
    pet_name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Photo URL')
    age = FloatField('Pet Age', validators=[InputRequired()])
    notes = StringField('Notes')

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    notes = StringField("Notes", validators=[Optional(), Length(min=10)])

    available = BooleanField("Available")
