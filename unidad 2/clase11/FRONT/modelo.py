import re
import requests

class Validador:
    @staticmethod
    def validarValor(valor):
        patronN = re.compile("^[5-9]\d{1,2}$|^[1-9]\d{3}$")
        resultadoN = patronN.match(valor) is not None
        return resultadoN

    @staticmethod
    def validarPeso(valorpeso):
        patronA = re.compile(r"^\d{1,3}(\.\d{0,2})?$")
        resultadoN = patronA.match(valorpeso)
        return resultadoN is not None

    @staticmethod
    def validarTamaño(valor):
        patronA = re.compile(r"^\d{1,2}(\.\d{0,2})?$")
        resultadoN = patronA.match(valor) is not None
        return resultadoN

    @staticmethod
    def validarcolor(valor):
        patronA = re.compile("^[A-Za-zñÑ ]*$")
        resultadoN = patronA.match(valor) is not None
        return resultadoN

class API:
    @staticmethod
    def guardar_moneda(moneda):
        data = {
            "valor": moneda.valor,
            "peso": moneda.peso,
            "tamaño": moneda.tamaño,
            "color": moneda.color
        }
        respuesta = requests.post("http://127.0.0.1:8000/v1/moneda", data)
        return respuesta

class Moneda:
    def __init__(self, valor, peso, tamaño, color):
        self.valor = valor
        self.peso = peso
        self.tamaño = tamaño
        self.color = color
