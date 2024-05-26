import re
from tkinter import *
from models.modelos import Cliente


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
    
    def validarCedula(valor):
        patronA = re.compile(r"^\d{1,3}(\.?\d{3}){2}$")
        resultadoN = patronA.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True
    

    def validarCorreo(valor):
        patronA = re.compile(r"^\w{3,}(\.\w{3,})*?@(gmail\.com|@hotmail\.com)$")
        resultadoN = patronA.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True
    
    def validarTelefono(valor):
        patronA = re.compile(r"^3\d{9}$")
        resultadoN = patronA.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True
    

    