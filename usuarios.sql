use Estudiante;

-- CREAR LOGIN 
CREATE LOGIN Hola WITH PASSWORD = 'Hola'


-- CREAR USUARIO
CREATE USER Hola FOR LOGIN Hola;

-- Permisos de CRUD
GRANT SELECT, INSERT, UPDATE, DELETE ON Estudiante TO Hola;