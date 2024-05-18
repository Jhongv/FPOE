import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/v1/persona'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self,nombre, apellido, estatura, peso):
        try:
            print(nombre, apellido, estatura,peso)
            data = {
                'nombre': nombre,
                'apellido': apellido,
                'estatura': int(estatura),
                'peso': int(peso)
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json)
            return resultado
        except:
            pass
    
    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        return resultado.json()
    
    def consultar_todo(self, nombre, apellido, estatura,peso):
        url = self.url+ "?"
        print(type(peso))
        if peso != '':
            url = url + 'id=' + str(peso) + "&"
        if nombre != '':
            url = url + 'nombre=' + str(nombre) + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()