from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class LoginForm(FlaskForm):
    username = StringField(
        "Nombre de usuario",  validators = [ InputRequired( message='Nombre requerido')])
    password = PasswordField(
        "clave",  validators = [ InputRequired( message='clave requerida')])
    submit = SubmitField(label = "iniciar sesión")