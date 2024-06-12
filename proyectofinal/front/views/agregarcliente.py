from tkinter import *
import tkinter as tk
from controler.controlador import Validaciones
from models.modelos import Cliente
import re
from tkinter import messagebox
import requests

class AgregarCliente:


    def __init__(self, menuSecundario):
        
        self.ventana = tk.Toplevel(menuSecundario)

    def mostrarInterfaz(self):
        
        def eventoVnombre(event):
            global nombre
            if Validaciones.validarNombre(cliente.nombre):
                textoVnombre = ""
            else:
                textoVnombre = "Nombre debe tener solo letras"
            lblErrorNombre.config(text=textoVnombre)

        def eventoVapellido(event):
            
            global apellido
            if Validaciones.validarApellido(cliente.apellido):
                textVapellido = ""
            else:
                textVapellido = "Apellido debe tener solo letras"
            lblErrorApellidoCliente.config(text=textVapellido)

        def eventoVCedula(event):
            
            global cedula
            if Validaciones.validarCedula(cliente.cedula):
                textoVCedula = ""
            else:
                textoVCedula = "Cédula debe tener entre 7 a 10 dígitos"
            lblErrorCedulaCliente.config(text=textoVCedula)

        def eventoVTelefono(event):
            
            global telefono
            if Validaciones.validarTelefono(cliente.telefono):
                textoVtelefono = ""
            else:
                textoVtelefono = "El teléfono debe empezar con el prefijo 3 y tener máximo 10 dígitos"
            lblErrorTelefonoCliente.config(text=textoVtelefono)

        def eventoVemail(event):
            
            global email
            if Validaciones.validarCorreo(cliente.email):
                textoVemail = ""
            else:
                textoVemail = "Debe ser con caracteres alfanuméricos antes del @ y con dominios gmail o hotmail.com"
            lblErrorEmailCliente.config(text=textoVemail)

        def validarInformacion():

            
            nombreV = re.match(r"^[A-Za-zñÑ ]*$", cliente.nombre.get())
            apellidoV = re.match(r"^[A-Za-zñÑ ]*$", cliente.apellido.get())
            cedula = re.match(r"^\d{1,3}(\.?\d{3}){2}$", cliente.cedula.get())
            telefono = re.match(r"^3\d{9}$", cliente.telefono.get())
            email = re.match(r"^\w{3,}(\.\w{3,})*?@(gmail\.com|hotmail\.com)$", cliente.email.get())

            if nombreV and apellidoV and cedula and telefono and email:
                data = {
                    "nombre": cliente.nombre.get(),
                    "apellido": cliente.apellido.get(),
                    "cedula": cliente.cedula.get(),
                    "telefono": cliente.telefono.get(),
                    "email": cliente.email.get()
                }
                respuesta = requests.post("http://127.0.0.1:8000/v1/cliente", data)
                print(respuesta.status_code)
                print(respuesta.content)
                
                messagebox.showinfo("Información", "Se guardó correctamente")

                txtNombreCliente.delete(0, tk.END)
                txtApellidoCliente.delete(0,tk.END)
                txtCedulaCliente.delete(0,tk.END)
                txtEmailCliente.delete(0,tk.END)
                txtTelefonoCliente.delete(0,tk.END)

            else:
                messagebox.showerror("Información", "No se pudo guardar, confirme si está correcto")

        self.ventana.focus_set()
        self.ventana.title("Agregar al cliente")
        self.ventana.resizable(0, 0)
        cliente = Cliente(self.ventana)

        # Marco del título
        marcoTitulo = LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=0, padx=10, pady=10)
        lblTitulo = Label(marcoTitulo, text="Agregar al Cliente")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        marco1 = LabelFrame(self.ventana)
        marco1.grid(row=1, column=0, padx=10, pady=10)

        lblNombreCliente = Label(marco1, text="Nombre*:")
        lblNombreCliente.grid(row=0, column=0)

        txtNombreCliente = Entry(marco1, textvariable=cliente.nombre)
        txtNombreCliente.grid(row=0, column=1)

        lblErrorNombre = Label(marco1, text='', fg="red")
        lblErrorNombre.grid(row=1, column=1)

        marco2 = LabelFrame(self.ventana)
        marco2.grid(row=2, column=0, padx=10, pady=10)

        lblApellidoCliente = Label(marco2, text="Apellido*:")
        lblApellidoCliente.grid(row=0, column=0)

        txtApellidoCliente = Entry(marco2, textvariable=cliente.apellido)
        txtApellidoCliente.grid(row=0, column=1)

        lblErrorApellidoCliente = Label(marco2, text='', fg="red")
        lblErrorApellidoCliente.grid(row=1, column=1)

        marco3 = LabelFrame(self.ventana)
        marco3.grid(row=3, column=0, padx=10, pady=10)

        lblCedulaCliente = Label(marco3, text="Cédula*:")
        lblCedulaCliente.grid(row=0, column=0)

        txtCedulaCliente = Entry(marco3, textvariable=cliente.cedula)
        txtCedulaCliente.grid(row=0, column=1)

        lblErrorCedulaCliente = Label(marco3, text='', fg="red")
        lblErrorCedulaCliente.grid(row=1, column=1)

        marco4 = LabelFrame(self.ventana)
        marco4.grid(row=4, column=0, padx=10, pady=10)

        lblTelefonoCliente = Label(marco4, text="Teléfono*:")
        lblTelefonoCliente.grid(row=0, column=0)

        txtTelefonoCliente = Entry(marco4, textvariable=cliente.telefono)
        txtTelefonoCliente.grid(row=0, column=1)

        lblErrorTelefonoCliente = Label(marco4, text='', fg="red")
        lblErrorTelefonoCliente.grid(row=1, column=1)

        marco5 = LabelFrame(self.ventana)
        marco5.grid(row=5, column=0, padx=10, pady=10)

        lblEmailCliente = Label(marco5, text="Email*:")
        lblEmailCliente.grid(row=0, column=0)

        txtEmailCliente = Entry(marco5, textvariable=cliente.email)
        txtEmailCliente.grid(row=0, column=1)

        lblErrorEmailCliente = Label(marco5, text='', fg="red")
        lblErrorEmailCliente.grid(row=1, column=1)

        btnGuardar = Button(self.ventana, text="Guardar", padx=10, pady=10, command=validarInformacion)
        btnGuardar.grid(row=6, column=0, padx=10, pady=10)

        txtNombreCliente.bind("<KeyRelease>", eventoVnombre)
        txtApellidoCliente.bind("<KeyRelease>", eventoVapellido)
        txtCedulaCliente.bind("<KeyRelease>", eventoVCedula)
        txtTelefonoCliente.bind("<KeyRelease>", eventoVTelefono)
        txtEmailCliente.bind("<KeyRelease>", eventoVemail)

        self.ventana.mainloop()
