import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://127.0.0.1:8000/v1/persona'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self,valor, peso, tamaño, color):
        try:
            print(valor, peso, tamaño,color)
            data = {
                'valor': valor,
                'peso': peso,
                'tamaño': int(tamaño),
                'color': int(color)
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json)
            return resultado
        except:
            pass


    def actualizar(self,id,valor, peso, tamaño, color):
        try:
            print(valor, peso, tamaño,color)
            data = {                
                'valor': valor,
                'peso': peso,
                'tamaño': int(tamaño),
                'color': int(color)
            }
            resultado = requests.put(self.url + '/' + id + '/', json=data)
            print(resultado.json)
            return resultado
        except:
            pass

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code
    
    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        return resultado.json()
    
    
    def consultar_todo(self, valor, peso, tamaño,color):
        url = self.url+ "?"
        print(type(color))
        if color != '':
            url = url + 'id=' + str(color) + "&"
        if valor != '':
            url = url + 'valor=' + str(valor) + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()