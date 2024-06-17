import requests
from tkinter import messagebox
class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/v1/cliente'
        self.url2= 'http://127.0.0.1:8000/v1/servicio'

    def guardar(self, nombre, apellido, cedula, telefono, email):
        
        try:
            print(nombre, apellido, cedula, telefono, email)
            data={
                'nombre': nombre,
                'apellido': apellido,
                'cedula': cedula,
                'telefono': telefono,
                'email': email
            }
            resultado=requests.post(self.url, json=data)
            print(resultado.json())
            return resultado
        except:
            pass

    def guardarServicio(self, cedula, nombreServicio, descripcion, precio):
        
        try:
            print(cedula, nombreServicio, descripcion, precio)
            data={
                'cedula': cedula,
                'nombreServicio': nombreServicio,
                'descripcion': descripcion,
                'precio': precio
            }
            resultado=requests.post(self.url2, json=data)
            print(resultado.json())
            return resultado
        except:
            pass   

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code
    
    def eliminarservicio(self, id):
        resultado = requests.delete(self.url2 + '/' + str(id))
        return resultado.status_code


    def consultar(self, cedula):
        resultado = requests.get(self.url + '?cedula=' + str(cedula))
        return resultado.json()
    
    def consultarServicio(self, cedula):
        resultado = requests.get(self.url2 + '?cedulaCliente=' + str(cedula))
        return resultado.json()

    
    def actualizar(self, id, nombre, apellido, cedula, telefono, email):
        
        try:
            print(nombre, apellido, cedula, telefono, email)
            data={
                'nombre': nombre,
                'apellido': apellido,
                'cedula': cedula,
                'telefono': telefono,
                'email': email
            }
            resultado=requests.put(self.url + '/' + id + '/', json=data)
            print(resultado.json())
            return resultado
        except:
            pass

    def actualizarServicio(self, id, cedula, nombreServicio, descripcion, precio):
        
        try:
            print(cedula, nombreServicio, descripcion, precio)
            data={
                'cedula': cedula,
                'nombreServicio': nombreServicio,
                'descripcion': descripcion,
                'precio': precio
            }
            resultado=requests.put(self.url2 + '/' + id + '/', json=data)
            print(resultado.json())
            return resultado
        except:
            pass

    def consultar_todo(self, nombre, apellido, cedula,telefono, email):
        url = self.url+ "?"
        print(type(cedula))
        if cedula != '':
            url = url + 'cedula=' + str(cedula) + "&"
        if nombre != '':
            url = url + 'nombre=' + str(nombre) + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()
    
    def consultar_todo_servicio(self, cedula, nombreServicio, descripcion, precio):
        try:
            url = self.url2 + "?"
            if cedula:
                url += f'cedula={cedula}&'
            if nombreServicio:
                url += f'nombreServicio={nombreServicio}&'
            if descripcion:
                url += f'descripcion={descripcion}&'
            if precio:
                url += f'precio={precio}&'
            url = url.rstrip('&')
            print(url)
            resultado = requests.get(url)
            return resultado.json()
        except Exception as e:
            print(f"Error: {e}")