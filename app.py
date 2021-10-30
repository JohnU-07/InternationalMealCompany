from functools import wraps
from sqlite3 import Error
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash,\
    session

# create the application object
app = Flask(__name__)
app.secret_key = "Team-9"


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


def sql_connection():
    try:
        conn = sqlite3.connect('./bd/database.db')
        print("SQL Connection established")
        return conn
    except Error:
        print("Error establish connection")


# @app.context_processor
# def context_processor():


@app.route('/')
@login_required
def Index():
    strsql = 'SELECT * FROM empleados'
    conn = sql_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(strsql)
    data = [dict(row) for row in cur.fetchall()]
    cur.close()
    return render_template('index.html', employee=data)


@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    return render_template('register.html')


@app.route('/show', methods=['GET', 'POST'])
@login_required
def show():
    conn = sql_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('SELECT * FROM empleados WHERE id=(SELECT id_empleado FROM\
                                                   usuarios WHERE usuario=?)',
                [session['current_user']])
    data = cur.fetchone()
    cur.close()
    print(session['current_user'])
    print(data)
    return render_template('show.html', employee=data)


# @app.route('/add_contact', methods=['POST', 'GET'])
# @login_required
# def add_employee():
#     conn = sql_connection()
#     cur = conn.cursor()
#     if request.method == 'POST':
#         fullname = request.form['fullname']
#         phone = request.form['phone']
#         email = request.form['email']
#         cur.execute(
#             "INSERT INTO empleados (name, email, phone) VALUES (?,?,?)",
#             [fullname, email, phone])
#         conn.commit()
#         flash('Empleado Agregado Exitosamente')
#         return redirect(url_for('Index'))

@app.route('/add_contact', methods=['POST', 'GET'])
@login_required
def add_employee():
    if request.method == 'POST':
        pNombre = request.form['pNombre']
        sNombre = request.form['sNombre']
        pApellido = request.form['pApellido']
        sApellido = request.form['sApellido']
        email = request.form['email']
        telefono = request.form['telefono']
        fechaIngreso = request.form['fechaIngreso']
        tipoContrato = request.form['tipoContrato']
        fechaTerminoContrato = request.form['fechaTerminoContrato']
        idDependencia = request.form['idDependencia']
        salario = request.form['salario']
        idCargo = request.form['idCargo']
        idTipoUsuario = request.form['idTipoUsuario']
        idTipoIdentificacion = request.form['idTipoIdentificacion']
        numeroIdentificacion = request.form['numeroIdentificacion']
        direccion = request.form['direccion']
        conn = sql_connection()
        cur = conn.cursor()
        cur.execute("""INSERT INTO empleados (primer_nombre,
                segundo_nombre,
                primer_apellido,
                segundo_apellido,
                email,
                telefono,
                fecha_ingreso,
                id_tipo_contrato,
                fecha_termino_contrato,
                id_dependencia,
                salario,
                id_cargo,
                id_tipo_usuario,
                id_tipo_identificacion,
                numero_identificacion,
                direccion)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    [pNombre, sNombre, pApellido, sApellido, email, telefono, fechaIngreso, tipoContrato, fechaTerminoContrato, idDependencia, salario, idCargo, idTipoUsuario, idTipoIdentificacion, numeroIdentificacion, direccion])
        conn.commit()
        flash('Empleado Agregado Exitosamente')
        return redirect(url_for('Index'))


@ app.route('/edit/<id>', methods=['POST', 'GET'])
@ login_required
def get_employee(id):
    conn = sql_connection()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('SELECT * FROM empleados WHERE id = ?', [id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', employee=data[0])


@ app.route('/update/<id>', methods=['POST'])
@ login_required
def update_employee(id):
    if request.method == 'POST':
        pNombre = request.form['pNombre']
        sNombre = request.form['sNombre']
        pApellido = request.form['pApellido']
        sApellido = request.form['sApellido']
        email = request.form['email']
        telefono = request.form['telefono']
        fechaIngreso = request.form['fechaIngreso']
        tipoContrato = request.form['tipoContrato']
        fechaTerminoContrato = request.form['fechaTerminoContrato']
        idDependencia = request.form['idDependencia']
        salario = request.form['salario']
        idCargo = request.form['idCargo']
        idTipoUsuario = request.form['idTipoUsuario']
        idTipoIdentificacion = request.form['idTipoIdentificacion']
        numeroIdentificacion = request.form['numeroIdentificacion']
        direccion = request.form['direccion']
        conn = sql_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE empleados
            SET primer_nombre = ?,
                segundo_nombre = ?,
                primer_apellido = ?,
                segundo_apellido = ?,
                email = ?,
                telefono = ?,
                fecha_ingreso = ?,
                id_tipo_contrato = ?,
                fecha_termino_contrato = ?,
                id_dependencia = ?,
                salario = ?,
                id_cargo = ?,
                id_tipo_usuario = ?,
                id_tipo_identificacion = ?,
                numero_identificacion = ?,
                direccion = ?
            WHERE id = ?
        """, [pNombre, sNombre, pApellido, sApellido, email, telefono,
              fechaIngreso, tipoContrato, fechaTerminoContrato,
              idDependencia, salario, idCargo, idTipoUsuario,
              idTipoIdentificacion, numeroIdentificacion, direccion, id])
    flash('Empleado Actualizado Exitosamente')
    conn.commit()
    return redirect(url_for('Index'))


@ app.route('/delete/<id>', methods=['POST', 'GET'])
@ login_required
def delete_employee(id):
    conn = sql_connection()
    cur = conn.cursor()

    cur.execute('DELETE FROM empleados WHERE id = {0}'.format(id))
    conn.commit()
    flash('Empleado Eliminado Exitosamente')
    return redirect(url_for('Index'))


# Route for handling the login page logic
@ app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    conn = sql_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur.execute(
            "SELECT * FROM usuarios WHERE usuario = ? AND password = ?",
            [username, password])
        Index(username)
        data = cur.fetchone()
        # Change username and password to test
        if not data:
            error = 'Credenciales invalidas. Por favor intente de nuevo.'
        else:
            session['logged_in'] = True
            session['current_user'] = username
            print("INFORMACION---------", data)
            session['id'] = data[4]
            return redirect(url_for('Index'))
    return render_template('login.html', error=error)


@ app.route('/logout')
@ login_required
def logout():
    session.pop('logged_in', None)
    flash('Usuario Deslogueado!')
    return redirect(url_for('login'))


# starting app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
