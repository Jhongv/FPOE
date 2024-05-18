import re
from tkinter import *
from modelos.usuario import Usuario

class Validaciones():

    
    def __init__(self):
        pass
    def validarNombre(valor):
        patronN = re.compile("^[A-Za-zñÑ ]*$")
        resultadoN = patronN.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True
    
    def validarApellido(valorApellido):
        patronA = re.compile("^[A-Za-zñÑ ]*$")
        resultadoN = patronA.match(valorApellido.get()) is not None
        if not resultadoN:
            return False
        return True
    
    def validarEstatura(valor):
        patronA = re.compile(r"^\d{1}(\.\d{0,2})?$")
        resultadoN = patronA.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True
    

    def validarPeso(valor):
        patronA = re.compile(r"^\d{1,3}(\.\d{0,2})?$")
        resultadoN = patronA.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True
    

    