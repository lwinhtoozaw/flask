from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators = [InputRequired('Username is required')])
    password = PasswordField('password', validators = [InputRequired('Password is required')])
    recaptcha = RecaptchaField('recaptcha', validators = [InputRequired('Recaptcha is required')])