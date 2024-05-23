from tkinter import *
import tkinter as tk
class AgregarCliente():
    def __init__(self, menuSecundario):
        self.ventana=tk.Toplevel(menuSecundario)
        

    #Marco del titulo
    def mostrarInterfaz(self):

        def validarInformacion():
            pass
        self.ventana.focus_set()
        self.ventana.title("Agregar al cliente")
        self.ventana.resizable(0,0)


    #Se establece el contenido del marco1
        marcoTitulo=LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=0, padx=10, pady=10)
        lblTitulo=Label(marcoTitulo, text="Agregar al Cliente")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)
    
    
        marco1=LabelFrame(self.ventana)
        marco1.grid(row=1, column=0, padx=10, pady=10)

        lblNombreCliente=Label(marco1, text="Nombre*:")
        lblNombreCliente.grid(row=0, column=0)

        txtNombreCliente=Entry(marco1)
        txtNombreCliente.grid(row=0,column=1)

        lblErrorNombre=Label(marco1, text='', fg="red")
        lblErrorNombre.grid(row=1,column=1)

        marco2=LabelFrame(self.ventana)
        marco2.grid(row=2, column=0, padx=10, pady=10)

        lblApellidoCliente=Label(marco2, text="Apellido*:")
        lblApellidoCliente.grid(row=0, column=0)

        txtApellidoCliente=Entry(marco2)
        txtApellidoCliente.grid(row=0, column=1)

        lblErrorApellidoCliente=Label(marco2, text='', fg="red")
        lblErrorApellidoCliente.grid(row=1, column=1)

        marco3=LabelFrame(self.ventana)
        marco3.grid(row=3, column=0, padx=10, pady=10)


        lblCedulaCliente=Label(marco3, text="Cédula*:")
        lblCedulaCliente.grid(row=0, column=0)

        txtCedulaCliente=Entry(marco3)
        txtCedulaCliente.grid(row=0, column=1)

        lblErrorCedulaCliente=Label(marco3, text='', fg="red")
        lblErrorCedulaCliente.grid(row=1, column=1)

        marco4=LabelFrame(self.ventana)
        marco4.grid(row=4, column=0, padx=10, pady=10)

        lblTelefonoCliente=Label(marco4, text="Teléfono*:")
        lblTelefonoCliente.grid(row=0, column=0)

        txtTelefonoCliente=Entry(marco4)
        txtTelefonoCliente.grid(row=0, column=1)

        lblErrorTelefonoCliente=Label(marco4, text='', fg="red")
        lblErrorTelefonoCliente.grid(row=1, column=1)

        marco5=LabelFrame(self.ventana)
        marco5.grid(row=5, column=0, padx=10, pady=10)

        lblEmailCliente=Label(marco5, text="Email*:")
        lblEmailCliente.grid(row=0, column=0)

        txtEmailCliente=Entry(marco5)
        txtEmailCliente.grid(row=0, column=1)

        lblErrorEmailCliente=Label(marco5, text='', fg="red")
        lblErrorEmailCliente.grid(row=1, column=1)


        btnGuardar=Button(self.ventana, text="Guardar", padx=10, pady=10,command=validarInformacion)
        btnGuardar.grid(row=6,column=0, padx=10, pady=10)




        self.ventana.mainloop()