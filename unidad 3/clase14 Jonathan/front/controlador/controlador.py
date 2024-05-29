from modelos.usuario import Usuario
import re
from tkinter import *

class ControladorMoneda:
    def __init__(self):
        pass
    def validarValoreventoVValor(valor):
        patronN = re.compile("^[A-Za-zñÑ ]*$")
        resultadoN = patronN.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True

    def validarPeso(valorPeso):
        patronA = re.compile("^[A-Za-zñÑ ]*$")
        resultadoN = patronA.match(valorPeso.get()) is not None
        if not resultadoN:
            return False
        return True

    def validarTamañoeventoVTamaño(valor):
        patronA = re.compile(r"^\d{1}(\.\d{0,2})?$")
        resultadoN = patronA.match(valor) is not None
        if not resultadoN:
            return False
        return True
    
    
    def validarColoreventoVColor(valor):
        patronA = re.compile(r"^\d{1,3}(\.\d{0,2})?$")
        resultadoN = patronA.match(valor) is not None
        if not resultadoN:
            return False
        return True

    

    