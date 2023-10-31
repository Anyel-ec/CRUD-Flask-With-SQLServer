import pyodbc # pip install pyodbc
# pip install flask
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def conexion_bd():
    try: 
        conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=localhost;'
                                'Database=Estudiante;'
                                'UID: Hola;'
                                'PWD: Hola;'
                                'Trusted_Connection=yes;')
        print("Conexion exitosa")
        return conn
    except Exception as e:
        print("Ocurrio un error al conectar a SQL Server: ", e)
        return None

@app.route('/', methods=['GET', 'POST'])
# Create
def crear ():
    estudiantes = obtener_estudiantes()
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        conn = conexion_bd()
        cursor = conn.cursor()
        cursor.execute(' INSERT INTO ESTUDIANTE VALUES (?,?,?)', (id, nombre, apellido))
        cursor.commit()
        conn.close()
        return jsonify({"message": "Estudiante creado con éxito"})
    return render_template('crear.html', estudiantes = estudiantes)

def obtener_estudiantes():
    conn = conexion_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ESTUDIANTE')
    estudiantes = cursor.fetchall()
    conn.close()
    return estudiantes

@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    conn = conexion_bd()
    cursor = conn.cursor()
    nuevo_nombre = request.form['nombre']
    nuevo_apellido = request.form['apellido']
    cursor.execute('UPDATE ESTUDIANTE SET nombre = ?, apellido = ? WHERE id = ?', (nuevo_nombre, nuevo_apellido, id))
    cursor.commit()
    conn.close()
    return jsonify({"message": "Actualización correcta"})

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    conn = conexion_bd()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM ESTUDIANTE WHERE id = ?', (id))
    cursor.commit()
    conn.close()
    return jsonify({"message": "Eliminación correcta"})

app.run(debug=True)