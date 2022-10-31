# import class FlaskForm from the package flask_wtf, an extension of flask
# import classes that reprent form fields from wtforms 
import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """ Class object represents a login form
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

class RequestForm(FlaskForm):
    """ Class object represents a request form
    """
    studentname = StringField('Student Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    contact = IntegerField('Student Phone Number')
    period = DateTimeField('Attachment Period')
    submit = SubmitField('Submit')