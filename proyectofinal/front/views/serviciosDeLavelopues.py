from tkinter import *
import tkinter as tk
from tkinter import ttk
import re
from controler.controlador import Validaciones
from models.modelos import Servicio
from models.modelos import Cliente
class ServiciosLaveloPues():
    def __init__(self, menuSecundario):
        self.ventana=tk.Toplevel(menuSecundario)
        self.listaServicios=[]

    def seleccionarServicio(self, event,listaServicios, txtCedula, cbxcomboServicio, lblprecio, txtPrecioestablecido, lblDescripcion,txtDescripcion):
        
        select=cbxcomboServicio.get()
        
        if select=="Lavado+Brillado+Aspirado":
            txtDescripcion.delete(0, tk.END)
            txtPrecioestablecido.delete(0, tk.END)
            txtDescripcion.insert(0, "Transforma tu auto:\nLavado, brillado y aspirado para un resplandor impecable\ny una frescura interior revitalizante.")
            txtPrecioestablecido.insert(0, "$1000")
            lblprecio.grid(row=0, column=0)
            txtPrecioestablecido.grid(row=0, column=1)
            lblDescripcion.grid(row=0, column=0)
            txtDescripcion.grid(row=0, column=1)

        elif select=="Lavado+Limpieza/Motor+Porcelanizado+Aspirado":
            txtDescripcion.delete(0, tk.END)
            txtPrecioestablecido.delete(0, tk.END)
            txtDescripcion.insert(0, "Revitaliza tu auto:\nLavado, limpieza de motor,\nporcelanizado y aspirado para un brillo y\nrendimiento excepcionales, dentro y fuera.")
            txtPrecioestablecido.insert(0, "$120000")
            lblprecio.grid(row=0, column=0)
            txtPrecioestablecido.grid(row=0, column=1)
            lblDescripcion.grid(row=0, column=0)
            txtDescripcion.grid(row=0, column=1)

        elif select=="Lavado+Brillado+Lavado/Cojinería":
            txtDescripcion.delete(0, tk.END)
            txtPrecioestablecido.delete(0, tk.END)
            txtDescripcion.insert(0, "Transforma tu auto:\nLavado exterior,\nbrillado y lavado de\ncojinería para un\nbrillo impecable y una comodidad renovada.")
            txtPrecioestablecido.insert(0, "$130000")
            lblprecio.grid(row=0, column=0)
            txtPrecioestablecido.grid(row=0, column=1)
            lblDescripcion.grid(row=0, column=0)
            txtDescripcion.grid(row=0, column=1)


        elif select == "Lavado Interno+Brillado/Lámparas":
            txtDescripcion.delete(0, tk.END)
            txtPrecioestablecido.delete(0, tk.END)
            txtDescripcion.insert(0, "Renueva tu auto por dentro:\nlavado interno, brillado de\nsuperficies y\nlamparaz para un\ninterior reluciente y acogedor.")
            txtPrecioestablecido.insert(0, "$450000")
            lblprecio.grid(row=0, column=0)
            txtPrecioestablecido.grid(row=0, column=1)
            lblDescripcion.grid(row=0, column=0)
            txtDescripcion.grid(row=0, column=1)
        
    

        
    def mostrarInterfaz(self):
        def eventoVCedula(event):
            global cedula
            if Validaciones.validarCedula(servicio.cedulaCliente):
                textoVCedula=""
            else:
                textoVCedula="Cédula debe tener entre 7 a 10 dígitos"
            lblErrorCedula.config(text=textoVCedula)
        
            
        self.ventana.focus_set()
        self.ventana.title("Servicios de LaveloPues")
        self.ventana.resizable(0,0)
        cliente=Cliente(self.ventana)
        servicio=Servicio(self.ventana)
        

        marcoTitulo=LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=0, padx=10, pady=10)
        lblTitulo=Label(marcoTitulo, text="Servicio 1")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        marco1=LabelFrame(self.ventana)
        marco1.grid(row=1, column=0, padx=10, pady=10)

        lblCedulaClienteAccSer=Label(marco1, text="CC del cliente\nque va ha acceder al servicio*:")
        lblCedulaClienteAccSer.grid(row=0, column=0)
        txtCedulaClienteAccSer=Entry(marco1, textvariable=servicio.cedulaCliente)
        txtCedulaClienteAccSer.grid(row=0, column=1)
        lblErrorCedula=Label(marco1, text="", fg="red")
        lblErrorCedula.grid(row=1, column=1)

        marco2=LabelFrame(self.ventana)
        marco2.grid(row=2, column=0, padx=10, pady=10)
        lblServicio=Label(marco2, text="Servicio*:")
        lblServicio.grid(row=0, column=0)
        cbxServicio=ttk.Combobox(marco2, values=["Lavado+Brillado+Aspirado","Lavado+Limpieza/Motor+Porcelanizado+Aspirado","Lavado+Brillado+Lavado/Cojinería","Lavado Interno+Brillado/Lámparas"], textvariable=servicio.nombreServicio)
        cbxServicio.grid(row=0, column=1)

        
        


        marco3=LabelFrame(self.ventana)
        marco3.grid(row=3, column=0, padx=10, pady=10)
        

        lblDescripcion=Label(marco3, text="Descripción:")
        lblDescripcion.grid_forget()
        txtDescripcion=ttk.Entry(marco3, justify=tk.CENTER, textvariable=servicio.descripcion)
        txtDescripcion.grid_forget()

        marco4=LabelFrame(self.ventana)
        marco4.grid(row=4, column=0, padx=10, pady=10)

        lblPalabraPrecio=Label(marco4, text="Valor:")
        lblPalabraPrecio.grid_forget()
        txtPrecio=ttk.Entry(marco4, justify=tk.CENTER, textvariable=servicio.precio)
        txtPrecio.grid_forget()

        

        cbxServicio.bind("<<ComboboxSelected>>", lambda event: self.seleccionarServicio(event,self.listaServicios, txtCedulaClienteAccSer, cbxServicio, lblPalabraPrecio, txtPrecio, lblDescripcion, txtDescripcion))
        txtCedulaClienteAccSer.bind("<KeyRelease>", eventoVCedula)        

        self.ventana.mainloop()