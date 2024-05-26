from tkinter import *
import tkinter as tk
from tkinter import ttk
import re
class Servicio1lvbrlasp():
    def __init__(self, menuSecundario):
        self.ventana=tk.Toplevel(menuSecundario)


    def mostrarInterfaz(self):
        self.ventana.focus_set()
        self.ventana.title("Servicios de LaveloPues")
        self.ventana.resizable(0,0)

        marcoTitulo=LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=0, padx=10, pady=10)
        lblTitulo=Label(marcoTitulo, text="Servicio 1")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        marco1=LabelFrame(self.ventana)
        marco1.grid(row=1, column=0, padx=10, pady=10)

        lblCedulaClienteAccSer=Label(marco1, text="CC del cliente\nque va ha acceder al servicio*:")
        lblCedulaClienteAccSer.grid(row=0, column=0)
        txtCedulaClienteAccSer=Entry(marco1)
        txtCedulaClienteAccSer.grid(row=0, column=1)

        marco2=LabelFrame(self.ventana)
        marco2.grid(row=2, column=0, padx=10, pady=10)

        lblServicioSolicitado=Label(marco2, text="El sevicio escogido fue:")
        lblServicioSolicitado.grid(row=0, column=0)
        txtServicioSolicitado=Entry(marco2, width=25)
        txtServicioSolicitado.insert(0, "Lavado+Brillado+Aspirado")
        txtServicioSolicitado.config(state="disabled")
        txtServicioSolicitado.grid(row=0, column=1, padx=15, pady=15)
        


        marco3=LabelFrame(self.ventana)
        marco3.grid(row=3, column=0, padx=10, pady=10)

        lblDescripcion=Label(marco3, text="Descripción:")
        lblDescripcion.grid(row=0, column=0, padx=10,pady=10)

        lblDescripcionEstablecida=Label(marco3, text="Transforma tu auto:\nLavado, brillado y aspirado\npara un resplandor impecable\ny una frescura interior\nrevitalizante.")
        lblDescripcionEstablecida.grid(row=0, column=1, padx=10,pady=10)
        
        
        marco4=LabelFrame(self.ventana)
        marco4.grid(row=4, column=0, padx=10, pady=10)

        lblValorServicio=Label(marco4, text="Valor en pesos col:")
        lblValorServicio.grid(row=0, column=0)
        txtValorServicio=ttk.Entry(marco4, justify=tk.CENTER)
        txtValorServicio.insert(0, "$120000")
        txtValorServicio.config(state="disabled")
        txtValorServicio.grid(row=0, column=1,padx=15, pady=15)

        self.ventana.mainloop()