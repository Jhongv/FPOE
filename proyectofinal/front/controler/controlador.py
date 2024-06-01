import re
from tkinter import *
from models.modelos import Cliente


class Validaciones:
    """
    Clase que contiene métodos estáticos para realizar validaciones comunes, como validar nombres, apellidos,
    cédulas, correos electrónicos y números de teléfono.
    """

    def __init__(self):
        """
        Constructor de la clase Validaciones.
        """
        pass

    def validarNombre(valor):
        """
        Valida que el valor proporcionado sea un nombre válido, compuesto únicamente por letras y espacios.

        Args:
            valor (str): El valor a validar.

        Returns:
            bool: True si el valor es válido, False de lo contrario.
        """
        patronN = re.compile("^[A-Za-zñÑ ]*$")
        resultadoN = patronN.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True

    def validarApellido(valorApellido):
        """
        Valida que el valor proporcionado sea un apellido válido, compuesto únicamente por letras y espacios.

        Args:
            valorApellido (str): El valor del apellido a validar.

        Returns:
            bool: True si el valor es válido, False de lo contrario.
        """
        patronA = re.compile("^[A-Za-zñÑ ]*$")
        resultadoN = patronA.match(valorApellido.get()) is not None
        if not resultadoN:
            return False
        return True

    def validarCedula(valor):
        """
        Valida que el valor proporcionado sea una cédula válida.

        Args:
            valor (str): El valor de la cédula a validar.

        Returns:
            bool: True si el valor es válido, False de lo contrario.
        """
        patronA = re.compile(r"^\d{1,3}(\.?\d{3}){2}$")
        resultadoN = patronA.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True

    def validarCorreo(valor):
        """
        Valida que el valor proporcionado sea un correo electrónico válido.

        Args:
            valor (str): El valor del correo electrónico a validar.

        Returns:
            bool: True si el valor es válido, False de lo contrario.
        """
        patronA = re.compile(r"^\w{3,}(\.\w{3,})*?@(gmail\.com|@hotmail\.com)$")
        resultadoN = patronA.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True

    def validarTelefono(valor):
        """
        Valida que el valor proporcionado sea un número de teléfono válido.

        Args:
            valor (str): El valor del número de teléfono a validar.

        Returns:
            bool: True si el valor es válido, False de lo contrario.
        """
        patronA = re.compile(r"^3\d{9}$")
        resultadoN = patronA.match(valor.get()) is not None
        if not resultadoN:
            return False
        return True
