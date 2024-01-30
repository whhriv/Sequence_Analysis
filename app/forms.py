from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class SequenceForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    isolate = StringField('Isolate', validators=[InputRequired()])
    gene = StringField('Gene')
    location = StringField('Location')
    lat = StringField('Latitude')
    long = StringField('Longitude')
    assension = StringField('Longitude')
    sequenceRAW = StringField('Sequence', validators=[InputRequired()])
    submit = SubmitField('Register')


class SingleSequenceForm(FlaskForm):
	sequenceDNA = TextAreaField('sequenceDNA')
