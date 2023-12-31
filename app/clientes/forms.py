from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,EmailField
from wtforms.validators import InputRequired, Email

class ClientForm():
    username = StringField(
        "Ingresa el nombre del usuario:", validators= [ InputRequired(message='nombre requerido')]
        )
    password = StringField(
        "Ingresa el password del usuario:", validators= [ InputRequired(message='password requerido')]
        )
    email = EmailField(
        "Ingresa el email del usuario:",
        validators= [ InputRequired(message='email requerido'), Email('El email es invalido recuerda que debe contener "@" y el "."')])
    
class NewClientForm(FlaskForm, ClientForm):
    submit = SubmitField("Guardar")

class EditClientForm(FlaskForm, ClientForm):
    Submit = SubmitField("Actualizar")