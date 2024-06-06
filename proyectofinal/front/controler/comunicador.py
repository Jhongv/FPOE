import requests

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
    
    def consultarTodoServicio(self, cedula, nombreServicio, descripcion,precio):
        url = self.url2+ "?"
        print(type(cedula))
        if cedula != '':
            url = url + 'cedula=' + str(cedula) + "&"
        if nombreServicio != '':
            url = url + 'nombreServicio=' + str(nombreServicio) + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()