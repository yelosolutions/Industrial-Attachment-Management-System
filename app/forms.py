# import class FlaskForm from the package flask_wtf, an extension of flask
# import classes that reprent form fields from wtforms 
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, BooleanField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """ Class object represents a login form
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')
    
class SignupForm(FlaskForm):
    """ Class object represents a login form
    """
    user = SelectField(u'Select one', choices=['Student Number', 'Staff Number'])
    usernumber = StringField('Student/Staff Number')
    new_password = PasswordField('New Password')
    confirm_password = PasswordField('Confirm Password')
    register = SubmitField('Register')

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