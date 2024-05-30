from tkinter import *
import tkinter as tk
from tkinter import ttk
from controler.controlador import Validaciones
from models.modelos import Cliente
class ActualizarCliente():

    def __init__(self, menuSecundario):
        self.ventana=tk.Toplevel(menuSecundario)


    def selectCombobox(self, event, combobox, lblNombre, txtNombre, lblApellido, txtApellido, lblCedula, txtCedula, lblTelefono, txtTelefono, lblEmail, txtEmail, lblErrorNombre, lblErrorApellido, lblErrorCedula, labelErrorEmail, lblErrorTelefono):
        select=combobox.get()
        if select == "Nombre":
            lblNombre.grid(row=0, column=0)
            txtNombre.grid(row=0, column=1)
            lblErrorNombre.grid(row=1, column=1)
            
        elif select=="Apellido":
            lblApellido.grid(row=0, column=0)
            txtApellido.grid(row=0, column=1)
            lblErrorApellido.grid(row=1, column=1)

        elif select=="Cédula":
            lblCedula.grid(row=0, column=0)
            txtCedula.grid(row=0, column=1)
            lblErrorCedula.grid(row=1, column=1)

        elif select=="Teléfono":
            lblTelefono.grid(row=0, column=0)
            txtTelefono.grid(row=0, column=1)
            lblErrorTelefono.grid(row=1, column=1)

        elif select == "Email":
            lblEmail.grid(row=0, column=0)
            txtEmail.grid(row=0, column=1)
            labelErrorEmail.grid(row=1, column=1)



    #Marco del titulo
    def mostrarInterfaz(self):

        def eventoVnombre(event):
            global nombre
            if Validaciones.validarNombre(cliente.nombre):
                textoVnombre=""
            else:
                textoVnombre="Nombre debe tener solo letras"
            lblErrorNombre.config(text=textoVnombre)

        def eventoVapellido(event):
            global apellido
            if Validaciones.validarApellido(cliente.apellido):
                textVapellido=""
            else:
                textVapellido="Apellido debe tener solo letras"
            lblErrorApellido.config(text=textVapellido)

        def eventoVCedula(event):
            global cedula
            if Validaciones.validarCedula(cliente.cedula):
                textoVCedula=""
            else:
                textoVCedula="Cédula debe tener entre 7 a 10 dígitos"
            lblErrorCedula.config(text=textoVCedula)

        def eventoVTelefono(event):
            global telefono
            if Validaciones.validarTelefono(cliente.telefono):
                textoVtelefono=""
            else:
                textoVtelefono="el teléfono debe empezar con el prefijo 3 y max 10 dígitos"
            lblErrorTelefono.config(text=textoVtelefono)

        def eventoVemail(event):
            global email
            if Validaciones.validarNombre(cliente.nombre):
                textoVemail=""
            else:
                textoVemail="Debe ser con carácteres alfanuméricos antes del @ y con dominios gmail o hotmail.com"
            lblErrorEmail.config(text=textoVemail)

        

        self.ventana.focus_set()
        self.ventana.title("Actualizar al cliente")
        self.ventana.resizable(0,0)
        cliente=Cliente(self.ventana)

    #Se establece el contenido del marco1
        marcoTitulo=LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=0, padx=10, pady=10)
        lblTitulo=Label(marcoTitulo, text="Actualizar al Cliente")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)
    
    
        marco1=LabelFrame(self.ventana)
        marco1.grid(row=1, column=0, padx=10, pady=10)

        lblSeleccionar=Label(marco1, text="Seleccione el campo que quiere modificar:")
        lblSeleccionar.grid(row=0, column=0, padx=5, pady=5)

        cbxSeleccionarCampoActualizar=ttk.Combobox(marco1, values=["Nombre", "Apellido", "Cédula", "Teléfono","Email"])
        cbxSeleccionarCampoActualizar.grid(row=0, column=1, padx=5, pady=5)



        marco2=LabelFrame(self.ventana)
        marco2.grid(row=2, column=0, padx=10, pady=10)


        lblNombreCliente=Label(marco2, text="Nombre*:")
        lblNombreCliente.grid_forget()

        txtNombreCliente=Entry(marco2, textvariable=cliente.nombre)
        txtNombreCliente.grid_forget()

        lblErrorNombre=Label(marco2, text="", fg="red")
        lblErrorNombre.grid_forget()

        marco3=LabelFrame(self.ventana)
        marco3.grid(row=3, column=0, padx=10, pady=10)


        lblApellidoCliente=Label(marco3, text="Apellido*:")
        lblApellidoCliente.grid_forget()

        txtApellidoCliente=Entry(marco3, textvariable=cliente.apellido)
        txtApellidoCliente.grid_forget()

        lblErrorApellido=Label(marco3, text="",fg="red")
        lblErrorApellido.grid_forget()

        marco4=LabelFrame(self.ventana)
        marco4.grid(row=4, column=0, padx=10, pady=10)

        lblCedulaCliente=Label(marco4, text="Cédula*:")
        lblCedulaCliente.grid_forget()

        txtCedulaCliente=Entry(marco4, textvariable=cliente.cedula)
        txtCedulaCliente.grid_forget()
        lblErrorCedula=Label(marco4, text="", fg="red")
        lblErrorCedula.grid_forget()

        marco5=LabelFrame(self.ventana)
        marco5.grid(row=5, column=0, padx=10, pady=10)

        lblTelefonoCliente=Label(marco5, text="Teléfono*:")
        lblTelefonoCliente.grid_forget()

        txtTelefonoCliente=Entry(marco5, textvariable=cliente.telefono)
        txtTelefonoCliente.grid_forget()
        lblErrorTelefono=Label(marco5, text="", fg="red")
        lblErrorTelefono.grid_forget()

        marco6=LabelFrame(self.ventana)
        marco6.grid(row=6, column=0, padx=10, pady=10)

        lblEmailCliente=Label(marco6, text="Email*:")
        lblEmailCliente.grid_forget()

        txtEmailCliente=Entry(marco6, textvariable=cliente.email)
        txtEmailCliente.grid_forget()
        lblErrorEmail=Label(marco6, text="", fg="red")
        lblErrorEmail.grid_forget()        


        btnActualizarDatosCliente=Button(self.ventana, text="Actualizar")
        btnActualizarDatosCliente.grid(row=7, column=0, padx=10, pady=10)
        cbxSeleccionarCampoActualizar.bind("<<ComboboxSelected>>", lambda event: self.selectCombobox(event, cbxSeleccionarCampoActualizar, lblNombreCliente, txtNombreCliente,lblApellidoCliente,
                                                                                                     txtApellidoCliente, lblCedulaCliente, txtCedulaCliente,lblTelefonoCliente, txtTelefonoCliente,
                                                                                                     lblEmailCliente, txtEmailCliente, lblErrorNombre, lblErrorApellido, lblErrorCedula, lblErrorEmail, lblErrorTelefono))
        
        txtNombreCliente.bind("<KeyRelease>", eventoVnombre)
        txtApellidoCliente.bind("<KeyRelease>", eventoVapellido)
        txtCedulaCliente.bind("<KeyRelease>", eventoVCedula)
        txtTelefonoCliente.bind("<KeyRelease>", eventoVTelefono)
        txtEmailCliente.bind("<KeyRelease>", eventoVemail)


        self.ventana.mainloop()