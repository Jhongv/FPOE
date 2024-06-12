from tkinter import *
import tkinter as tk
from tkinter import ttk
from controler.controlador import Validaciones
from models.modelos import Cliente
from controler.comunicador import Comunicacion
from tkinter import messagebox
from .tabla import Tabla

class ActualizarCliente:


    def __init__(self, menuSecundario):

        titulos=['Identificador','Nombre','Apellido','Cédula','Teléfono','Email']
        columnas=['id', 'nombre', 'apellido', 'cedula', 'telefono', 'email']
        data=[]
        self.ventana = tk.Toplevel(menuSecundario)
        self.comunicador=Comunicacion(self.ventana)
        self.tabla=Tabla(self.ventana, titulos, columnas, data)
        self.cargar_tabla()

    def cargar_tabla(self):
        resultado=self.comunicador.consultar_todo('','','','','')
        data=[]
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('nombre'), elemento.get('apellido'), elemento.get('cedula'), elemento.get('telefono'), elemento.get('email')))
        self.tabla.refrescar(data)
    

    def actualizar(self,id, nombre, apellido, cedula, telefono, email, txtid,txtn, txta, txtc, txttf, txte):
        if not id or not nombre or not apellido or not cedula or not telefono or not email:
            messagebox.showerror("ERROR", "Deben estar completos todos los campos")
        else:
            self.comunicador.actualizar(id, nombre, apellido, cedula, telefono, email)
            messagebox.showinfo("Información","Datos actualizados correctamente")
            txtid.delete(0, tk.END)
            txtn.delete(0, tk.END)
            txta.delete(0, tk.END)
            txtc.delete(0, tk.END)
            txttf.delete(0, tk.END)
            txte.delete(0,tk.END)

    def selectCombobox(self, event, combobox, lblNombre, txtNombre, lblApellido, txtApellido, lblCedula, txtCedula, lblTelefono, txtTelefono, lblEmail, txtEmail, lblErrorNombre, lblErrorApellido, lblErrorCedula, lblErrorEmail, lblErrorTelefono):

        select = combobox.get()
        if select == "Nombre":
            lblNombre.grid(row=0, column=0)
            txtNombre.grid(row=0, column=1)
            lblErrorNombre.grid(row=1, column=1)
            
        elif select == "Apellido":
            lblApellido.grid(row=0, column=0)
            txtApellido.grid(row=0, column=1)
            lblErrorApellido.grid(row=1, column=1)

        elif select == "Cédula":
            lblCedula.grid(row=0, column=0)
            txtCedula.grid(row=0, column=1)
            lblErrorCedula.grid(row=1, column=1)

        elif select == "Teléfono":
            lblTelefono.grid(row=0, column=0)
            txtTelefono.grid(row=0, column=1)
            lblErrorTelefono.grid(row=1, column=1)

        elif select == "Email":
            lblEmail.grid(row=0, column=0)
            txtEmail.grid(row=0, column=1)
            lblErrorEmail.grid(row=1, column=1)

        else:
            messagebox.showerror("ERROR","Campo asignado no reconocido")
            
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
            lblErrorApellido.config(text=textVapellido)

        def eventoVCedula(event):

            global cedula
            if Validaciones.validarCedula(cliente.cedula):
                textoVCedula = ""
            else:
                textoVCedula = "Cédula debe tener entre 7 a 10 dígitos"
            lblErrorCedula.config(text=textoVCedula)

        def eventoVTelefono(event):
            
            global telefono
            if Validaciones.validarTelefono(cliente.telefono):
                textoVtelefono = ""
            else:
                textoVtelefono = "El teléfono debe empezar con el prefijo 3 y tener máximo 10 dígitos"
            lblErrorTelefono.config(text=textoVtelefono)

        def eventoVemail(event):

            global email
            if Validaciones.validarEmail(cliente.email):
                textoVemail = ""
            else:
                textoVemail = "Debe ser con caracteres alfanuméricos antes del @ y con dominios gmail o hotmail.com"
            lblErrorEmail.config(text=textoVemail)

        self.ventana.focus_set()
        self.ventana.title("Actualizar al cliente")
        self.ventana.resizable(0, 0)
        cliente = Cliente(self.ventana)

        # Marco del título
        marcoTitulo = LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=1, padx=10, pady=10)
        lblTitulo = Label(marcoTitulo, text="Actualizar al Cliente")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)
    
        marco1 = LabelFrame(self.ventana)
        marco1.grid(row=1, column=1, padx=10, pady=10)

        lblInfoSelectBtnAct=Label(marco1, text="Debe presionar este botón primero, para que visualize la información que desea modificar.")
        lblInfoSelectBtnAct.grid(row=0, column=0)


        marco2 = LabelFrame(self.ventana)
        marco2.grid(row=2, column=1, padx=10, pady=10)

        lblSeleccionar = Label(marco2, text="Seleccione el campo que quiere modificar:")
        lblSeleccionar.grid(row=0, column=0, padx=5, pady=5)

        cbxSeleccionarCampoActualizar = ttk.Combobox(marco2, values=["Nombre", "Apellido", "Cédula", "Teléfono", "Email"])
        cbxSeleccionarCampoActualizar.grid(row=0, column=1, padx=5, pady=5)

        marco3 = LabelFrame(self.ventana)
        marco3.grid(row=3, column=1, padx=10, pady=10)

        lblNombreCliente = Label(marco3, text="Nombre*:")
        lblNombreCliente.grid_forget()

        txtNombreCliente = Entry(marco3, textvariable=cliente.nombre)
        txtNombreCliente.grid_forget()

        lblErrorNombre = Label(marco3, text="", fg="red")
        lblErrorNombre.grid_forget()

        marco4 = LabelFrame(self.ventana)
        marco4.grid(row=4, column=1, padx=10, pady=10)

        lblApellidoCliente = Label(marco4, text="Apellido*:")
        lblApellidoCliente.grid_forget()

        txtApellidoCliente = Entry(marco4, textvariable=cliente.apellido)
        txtApellidoCliente.grid_forget()

        lblErrorApellido = Label(marco4, text="", fg="red")
        lblErrorApellido.grid_forget()

        marco5 = LabelFrame(self.ventana)
        marco5.grid(row=5, column=1, padx=10, pady=10)

        lblCedulaCliente = Label(marco5, text="Cédula*:")
        lblCedulaCliente.grid_forget()

        txtCedulaCliente = Entry(marco5, textvariable=cliente.cedula)
        txtCedulaCliente.grid_forget()

        lblErrorCedula = Label(marco5, text="", fg="red")
        lblErrorCedula.grid_forget()

        marco6 = LabelFrame(self.ventana)
        marco6.grid(row=6, column=1, padx=10, pady=10)

        lblTelefonoCliente = Label(marco6, text="Teléfono*:")
        lblTelefonoCliente.grid_forget()

        txtTelefonoCliente = Entry(marco6, textvariable=cliente.telefono)
        txtTelefonoCliente.grid_forget()

        lblErrorTelefono = Label(marco6, text="", fg="red")
        lblErrorTelefono.grid_forget()

        marco7 = LabelFrame(self.ventana)
        marco7.grid(row=7, column=1, padx=10, pady=10)

        lblEmailCliente = Label(marco7, text="Email*:")
        lblEmailCliente.grid_forget()

        txtEmailCliente = Entry(marco7, textvariable=cliente.email)
        txtEmailCliente.grid_forget()

        lblErrorEmail = Label(marco7, text="", fg="red")
        lblErrorEmail.grid_forget()

        marco8 = LabelFrame(self.ventana)
        marco8.grid(row=8, column=1, padx=10, pady=10)

        txtId=Entry(marco8)
        txtId.grid(row=0, column=0)

        btnActualizarDatosCliente = Button(self.ventana, text="Actualizar", command=lambda:self.actualizar(txtId.get(), txtNombreCliente.get(), txtApellidoCliente.get(), txtCedulaCliente.get(), txtTelefonoCliente.get(), txtEmailCliente.get(), txtId,txtNombreCliente, txtApellidoCliente, txtCedulaCliente, txtTelefonoCliente, txtEmailCliente))
        btnActualizarDatosCliente.grid(row=7, column=1, padx=10, pady=10)

        
        self.tabla.tabla.grid(row=9, column=0, columnspan=3)

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                txtId.delete(0, END)
                txtId.insert(0, str(valores[0]))
                txtNombreCliente.delete(0, END)
                txtNombreCliente.insert(0, str(valores[1]))
                txtApellidoCliente.delete(0, END)
                txtApellidoCliente.insert(0, str(valores[2]))
                txtCedulaCliente.delete(0, END)
                txtCedulaCliente.insert(0, str(valores[3]))
                txtTelefonoCliente.delete(0, END)
                txtTelefonoCliente.insert(0, str(valores[4]))
                txtEmailCliente.delete(0, END)
                txtEmailCliente.insert(0, str(valores[5]))



        #EVENTOS
        cbxSeleccionarCampoActualizar.bind("<<ComboboxSelected>>", lambda event: self.selectCombobox(
            event, cbxSeleccionarCampoActualizar, lblNombreCliente, txtNombreCliente, lblApellidoCliente,
            txtApellidoCliente, lblCedulaCliente, txtCedulaCliente, lblTelefonoCliente, txtTelefonoCliente,
            lblEmailCliente, txtEmailCliente, lblErrorNombre, lblErrorApellido, lblErrorCedula, lblErrorEmail, lblErrorTelefono))        
        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        txtNombreCliente.bind("<KeyRelease>", eventoVnombre)
        txtApellidoCliente.bind("<KeyRelease>", eventoVapellido)
        txtCedulaCliente.bind("<KeyRelease>", eventoVCedula)
        txtTelefonoCliente.bind("<KeyRelease>", eventoVTelefono)
        txtEmailCliente.bind("<KeyRelease>", eventoVemail)

        self.ventana.mainloop()
