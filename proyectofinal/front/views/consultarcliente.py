from tkinter import *
import tkinter as tk
from controler.controlador import Validaciones
from models.modelos import Cliente
class ConsultarCliente():
    def __init__(self, menuSecundario):
        self.ventana=tk.Toplevel(menuSecundario)
        

    #Marco del titulo
    def mostrarInterfaz(self):
        def eventoVCedula(event):
            global cedula
            if Validaciones.validarCedula(cliente.cedula):
                textoVCedula=""
            else:
                textoVCedula="Cédula debe tener entre 7 a 10 dígitos"
            lblErrorCedula.config(text=textoVCedula)


        self.ventana.focus_set()
        self.ventana.title("Eliminar al cliente")
        self.ventana.resizable(0,0)
        cliente=Cliente(self.ventana)

    #Se establece el contenido del marco1
        marcoTitulo=LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=0, padx=10, pady=10)
        lblTitulo=Label(marcoTitulo, text="Consultar Cliente")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)
    
    
        marco1=LabelFrame(self.ventana)
        marco1.grid(row=1, column=0, padx=10, pady=10)

        lblCedulaCliente=Label(marco1, text="Cédula*:")
        lblCedulaCliente.grid(row=0, column=0, padx=5, pady=5)

        txtCedulaCliente=Entry(marco1, textvariable=cliente.cedula)
        txtCedulaCliente.grid(row=0,column=1, padx=5, pady=5)

        lblErrorCedula=Label(marco1, text='', fg="red")
        lblErrorCedula.grid(row=1,column=1)

        btnConsultar=Button(self.ventana, text="Consultar", padx=5, pady=5)
        btnConsultar.grid(row=7,column=0, padx=5, pady=5)

        txtCedulaCliente.bind("<KeyRelease>", eventoVCedula)

        self.ventana.mainloop()