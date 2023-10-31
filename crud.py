import pyodbc # pip install pyodbc

try: 
    conn = pyodbc.connect('Driver={SQL Server};'
                            'Server=localhost;'
                            'Database=Estudiante;'
                            'UID: Hola;'
                            'PWD: Hola;'
                            'Trusted_Connection=yes;')
    print("Conexion exitosa")
except Exception as e:
    print("Ocurrio un error al conectar a SQL Server: ", e)
    
# Create
def crear (id, nombre, apellido):
    cursor = conn.cursor()
    cursor.execute(' INSERT INTO ESTUDIANTE VALUES (?,?,?)', (id, nombre, apellido))
    cursor.commit()
    print("Estudiante creado con exito")
    conn.close()
   

# Leer 
def leer ():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ESTUDIANTE')
    for row in cursor:
        print(row)
    cursor.close()
# Actualizar
def actualizar (id, nombre, apellido):
    cursor = conn.cursor()
    cursor.execute('UPDATE ESTUDIANTE SET nombre = ?, apellido = ? WHERE id = ?', (nombre, apellido, id))
    cursor.commit()
    print("Estudiante actualizado con exito")
    cursor.close()
# Eliminar
def eliminar  (id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM ESTUDIANTE WHERE id = ?', (id))
    cursor.commit()
    print("Estudiante eliminado con exito")
    cursor.close()

eliminar(1)
leer()

