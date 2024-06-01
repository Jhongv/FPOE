from tkinter import *
import tkinter as tk
from models.modelos import Cliente
from controler.controlador import Validaciones

class EliminarCliente:
    """
    Clase que representa la interfaz gráfica para eliminar un cliente.
    """

    def __init__(self, menuSecundario):
        """
        Inicializa una nueva ventana secundaria.

        Args:
            menuSecundario (Tk): La ventana principal o secundaria desde la cual se abre esta interfaz.
        """
        self.ventana = tk.Toplevel(menuSecundario)

    def mostrarInterfaz(self):
        """
        Configura y muestra la interfaz gráfica para eliminar un cliente.
        """
        def eventoVCedula(event):
            """
            Valida la cédula del cliente en tiempo real y muestra un mensaje de error si es inválida.

            Args:
                event (Event): El evento de liberación de una tecla en el campo de entrada de la cédula.
            """
            global cedula
            if Validaciones.validarCedula(cliente.cedula):
                textoVCedula = ""
            else:
                textoVCedula = "Cédula debe tener entre 7 a 10 dígitos"
            lblErrorCedula.config(text=textoVCedula)

        self.ventana.focus_set()
        self.ventana.title("Eliminar Cliente")
        self.ventana.resizable(0, 0)
        cliente = Cliente(self.ventana)

        # Marco del título
        marcoTitulo = LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=0, padx=10, pady=10)
        lblTitulo = Label(marcoTitulo, text="Eliminar Cliente")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        marco1 = LabelFrame(self.ventana)
        marco1.grid(row=1, column=0, padx=10, pady=10)

        lblCedulaCliente = Label(marco1, text="Cédula*:")
        lblCedulaCliente.grid(row=0, column=0, padx=5, pady=5)

        txtCedulaCliente = Entry(marco1, textvariable=cliente.cedula)
        txtCedulaCliente.grid(row=0, column=1, padx=5, pady=5)

        lblErrorCedula = Label(marco1, text='', fg="red")
        lblErrorCedula.grid(row=1, column=1)

        btnEliminar = Button(self.ventana, text="Eliminar", padx=5, pady=5)
        btnEliminar.grid(row=6, column=0, padx=5, pady=5)

        btnConsultar = Button(self.ventana, text="Consultar", padx=5, pady=5)
        btnConsultar.grid(row=7, column=0, padx=5, pady=5)

        txtCedulaCliente.bind("<KeyRelease>", eventoVCedula)

        self.ventana.mainloop()
