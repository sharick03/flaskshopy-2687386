from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class LoginForm(FlaskForm):
    username = StringField(label = "nombre de usuario",  validators = [ InputRequired( message='nombre requerido')])
    password = PasswordField(label = "clave",  validators = [ InputRequired( message='clave requerido')])
    submit = SubmitField(label = "iniciar sesión")


