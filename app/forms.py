# import class FlaskForm from the package flask_wtf, an extension of flask
# import classes that reprent form fields from wtforms 
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    """ Class object represents a login form
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')
    
class RegistrationForm(FlaskForm):
    """ Class object represents a login form
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please user a different email')

class StudentForm(FlaskForm):
    """ Class object represents a student form
    """
    username = StringField('Username', validators=[DataRequired()])
    adm_number = StringField('Student Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    date_added = DateTimeField('Date Added')
    submit = SubmitField('Submit')

class RequestForm(FlaskForm):
    """ Class object represents a request form
    """
    studentname = StringField('Student Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    contact = IntegerField('Student Phone Number')
    period = DateTimeField('Attachment Period')
    submit = SubmitField('Submit')
    
class NamerForm(FlaskForm):
    """ Class object represents a request form
    """
    name = StringField('Student Name', validators=[DataRequired()])
    submit = SubmitField('Submit')