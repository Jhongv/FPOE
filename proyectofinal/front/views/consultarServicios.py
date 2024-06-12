from tkinter import *
import tkinter as tk
from controler.controlador import Validaciones
from models.modelos import Servicio
from .tabla import Tabla
from controler.comunicador import Comunicacion

class ConsultarServicios:


    def __init__(self, menuSecundario):

        
        self.ventana = tk.Toplevel(menuSecundario)
        self.comunicador=Comunicacion(self.ventana)
        pass


    def accion_consultar_boton(self, cedulaCliente):
        resultado = self.comunicador.consultarServicio(cedulaCliente)
        print(resultado)
        print(type(resultado))


    def mostrarInterfaz(self):

        def eventoVCedula(event):

            global cedula
            if Validaciones.validarCedula(servicio.cedulaCliente):
                textoVCedula = ""
            else:
                textoVCedula = "Cédula debe tener entre 7 a 10 dígitos"
            lblErrorCedula.config(text=textoVCedula)



        self.ventana.focus_set()
        self.ventana.title("Consultar Servicio")
        self.ventana.resizable(0, 0)
        servicio = Servicio(self.ventana)

        # Marco del título
        marcoTitulo = LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=0, padx=10, pady=10)
        lblTitulo = Label(marcoTitulo, text="Consultar Servicio")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        marco1 = LabelFrame(self.ventana)
        marco1.grid(row=1, column=0, padx=10, pady=10)

        lblCedulaCliente = Label(marco1, text="Cédula*:")
        lblCedulaCliente.grid(row=0, column=0, padx=5, pady=5)

        txtCedulaCliente = Entry(marco1, textvariable=servicio.cedulaCliente)
        txtCedulaCliente.grid(row=0, column=1, padx=5, pady=5)

        lblErrorCedula = Label(marco1, text='', fg="red")
        lblErrorCedula.grid(row=1, column=1)

        btnConsultar = Button(self.ventana, text="Consultar", padx=5, pady=5, command = lambda: self.accion_consultar_boton(txtCedulaCliente.get()))
        btnConsultar.grid(row=7, column=0, padx=5, pady=5)
        

        txtCedulaCliente.bind("<KeyRelease>", eventoVCedula)

        self.ventana.mainloop()