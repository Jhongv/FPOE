import mysql.connector

def insertar_persona(nombre, apellido, edad, cedula):
    conexion = None
    cursor = None
    
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia esto a tu usuario de MySQL
            password="",  # Cambia esto a tu contraseña de MySQL (dejar en blanco si usas XAMPP por defecto)
            database="clase_15"  # Asegúrate de que esta es tu base de datos
        )

        cursor = conexion.cursor()
        sql = "INSERT INTO Persona (nombre, apellido, edad, cedula) VALUES (%s, %s, %s, %s)"
        valores = (nombre, apellido, edad, cedula)
        cursor.execute(sql, valores)

        conexion.commit()
        print("Registro insertado con éxito")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()

# Ejemplo de uso
insertar_persona("Juan", "Perez", 30, 12345678)

import mysql.connector

def actualizar_persona(cedula, nombre=None, apellido=None, edad=None):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="clase_15"
        )
        
        cursor = conexion.cursor()
        campos = []
        valores = []
        
        if nombre:
            campos.append("nombre = %s")
            valores.append(nombre)
        if apellido:
            campos.append("apellido = %s")
            valores.append(apellido)
        if edad:
            campos.append("edad = %s")
            valores.append(edad)
        
        valores.append(cedula)
        sql = f"UPDATE Persona SET {', '.join(campos)} WHERE cedula = %s"
        cursor.execute(sql, valores)
        
        conexion.commit()
        print("Registro actualizado con éxito")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        conexion.close()

# Ejemplo de uso
actualizar_persona(cedula=11111111, nombre="Juan Carlos", apellido="Escobar", edad=31)

import mysql.connector

def borrar_persona(cedula):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="clase_15"
        )
        
        cursor = conexion.cursor()
        sql = "DELETE FROM Persona WHERE cedula = %s"
        valores = (cedula,)
        cursor.execute(sql, valores)
        
        conexion.commit()
        print("Registro borrado con éxito")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        conexion.close()

# Ejemplo de uso
borrar_persona(12345678)

import mysql.connector

def consultar_persona(cedula):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="clase_15"
        )
        
        cursor = conexion.cursor()
        sql = "SELECT nombre, apellido, edad, cedula FROM Persona WHERE cedula = %s"
        valores = (cedula,)
        cursor.execute(sql, valores)
        
        resultado = cursor.fetchone()
        
        if resultado:
            print(f"Nombre: {resultado[0]}, Apellido: {resultado[1]}, Edad: {resultado[2]}, Cédula: {resultado[3]}")
        else:
            print("No se encontró ningún registro con esa cédula")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        conexion.close()

# Ejemplo de uso
consultar_persona(12345678)
