from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired
from wtforms.widgets.core import TextArea

class Registro(FlaskForm):
    pnombre = StringField('Primer Nombre', validators=[DataRequired(message='No dejar vacío, completar')])
    snombre = StringField('Segundo Nombre')
    papellido = StringField('Primer Apellido', validators=[DataRequired(message='No dejar vacío, completar')])
    sapellido = StringField('Segundo Apellido')
    tipoid = SelectField('Tipo de Identificación', choices=[('0', '--Tipo Id--'), ('1', 'Cédula de Ciudadanía'), ('2', 'Cédula de Extranjería'), ('3', 'Carné Diplomatico'), ('4', 'Pasaporte'), ('5', 'Tarjeta de Identidad')], validators=[DataRequired(message='No dejar vacío, completar')])
    idNum = StringField('Número de Identificación', validators=[DataRequired(message='No dejar vacío, completar')])
    fnacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired(message='No dejar vacío, completar')], format='%Y-%m-%d')
    email = StringField('E-mail')
    direccion = StringField('Dirección')
    telefono = StringField('Teléfono')
    enviar = SubmitField('Registrar')

class Retroalimentacion(FlaskForm):
    retroalimtext=TextAreaField("Retroalimentacion")
    puntajetext=StringField("Puntaje")

class Cambio_pass(FlaskForm):
    actualpass=PasswordField("Contraseña actual")
    nuevopass=PasswordField("Nueva contraseña")
    val_nuevopass=PasswordField("Confirme nueva contraseña")

class Info_personal(FlaskForm):
    pnombre = StringField('Primer Nombre')
    snombre = StringField('Segundo Nombre')
    papellido = StringField('Primer Apellido')
    sapellido = StringField('Segundo Apellido')
    tipoid = SelectField('Tipo de Identificación', choices=[('0', '--Tipo Id--'), ('1', 'Cédula de Ciudadanía'), ('2', 'Cédula de Extranjería'), ('3', 'Carné Diplomatico'), ('4', 'Pasaporte'), ('5', 'Tarjeta de Identidad')])
    idNum = StringField('Número de Identificación')
    fnacimiento = DateField('Fecha de Nacimiento')
    email = StringField('E-mail')
    direccion = StringField('Dirección')
    telefono = StringField('Teléfono')
    actualizar = SubmitField('Actualizar')
    eliminar = SubmitField('Eliminar Registro')



