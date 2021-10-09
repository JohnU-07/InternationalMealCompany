from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

class FormIndex(FlaskForm):
    pnombre = StringField('Primer Nombre', validators=[DataRequired(message='No dejar vacío, completar')])
    snombre = StringField('Segundo Nombre')
    papellido = StringField('Primer Apellido', validators=[DataRequired(message='No dejar vacío, completar')])
    sapellido = StringField('Segundo Apellido')
    tipoid = SelectField('Tipo de Identificación', choices=[('0', '--Seleccione el Tipo de Id--'), ('1', 'Cédula de Ciudadanía'), ('2', 'Cédula de Extranjería'), ('3', 'Carné Diplomatico'), ('4', 'Pasaporte'), ('5', 'Tarjeta de Identidad'), ('6', 'Número Único de Identificación'), ('7', 'Permiso Especial de Permanencia'), ('8', 'Salvoconducto de Permanencia')], validators=[DataRequired(message='No dejar vacío, completar')])
    idNum = StringField('Número de Identificación', validators=[DataRequired(message='No dejar vacío, completar')])
    fnacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired(message='No dejar vacío, completar')], format='%Y-%m-%d')
    email = StringField('E-mail')
    direccion = StringField('Dirección')
    telefono = StringField('Teléfono')
    enviar = SubmitField('Registrar')

