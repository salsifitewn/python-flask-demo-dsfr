from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField

class RegisterForm(FlaskForm):

    username = StringField(label='User Name:')
    email_address = StringField(label='Email Adress:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirm password:')
    submit= SubmitField(label='Create Account')