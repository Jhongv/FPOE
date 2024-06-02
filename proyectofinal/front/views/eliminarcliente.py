from tkinter import *
import tkinter as tk
from models.modelos import Cliente
from controler.controlador import Validaciones
from .tabla import Tabla
from controler.comunicador import Comunicacion

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
        titulos=['Identificador','Nombre','Apellido','Cédula','Teléfono','Email']
        columnas=['id', 'nombre', 'apellido', 'cedula', 'telefono', 'email']
        data=[]
        self.ventana = tk.Toplevel(menuSecundario)
        self.comunicador=Comunicacion(self.ventana)
        self.tabla=Tabla(self.ventana, titulos, columnas, data)
        self.ventana = tk.Toplevel(menuSecundario)
        pass

        


    def accion_consultar_todo(self, nombre, apellido, cedula, telefono, email):
        resultado=self.comunicador.consultar_todo(nombre, apellido, cedula, telefono, email)
        data=[]
        for elemento in resultado:
            data.append((elemento.get('id'),elemento.get('nombre'),elemento.get('apellido'),elemento.get('cedula'),elemento.get('telefono'), elemento.get('email')))
        self.tabla.refrescar(data)


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

        marco2 = LabelFrame(self.ventana)
        marco2.grid(row=2, column=0, padx=10, pady=10)

        lblNombreCliente = Label(marco2, text="Nombre*:")
        lblNombreCliente.grid_forget()

        txtNombreCliente = Entry(marco2, textvariable=cliente.nombre)
        txtNombreCliente.grid_forget()

        lblErrorNombre = Label(marco2, text="", fg="red")
        lblErrorNombre.grid_forget()

        marco3 = LabelFrame(self.ventana)
        marco3.grid(row=3, column=0, padx=10, pady=10)

        lblApellidoCliente = Label(marco3, text="Apellido*:")
        lblApellidoCliente.grid_forget()

        txtApellidoCliente = Entry(marco3, textvariable=cliente.apellido)
        txtApellidoCliente.grid_forget()

        lblErrorApellido = Label(marco3, text="", fg="red")
        lblErrorApellido.grid_forget()

        marco4 = LabelFrame(self.ventana)
        marco4.grid(row=4, column=0, padx=10, pady=10)

        lblTelefonoCliente = Label(marco4, text="Teléfono*:")
        lblTelefonoCliente.grid_forget()

        txtTelefonoCliente = Entry(marco4, textvariable=cliente.telefono)
        txtTelefonoCliente.grid_forget()

        lblErrorTelefono = Label(marco4, text="", fg="red")
        lblErrorTelefono.grid_forget()

        marco5 = LabelFrame(self.ventana)
        marco5.grid(row=6, column=0, padx=10, pady=10)

        lblEmailCliente = Label(marco5, text="Email*:")
        lblEmailCliente.grid_forget()

        txtEmailCliente = Entry(marco5, textvariable=cliente.email)
        txtEmailCliente.grid_forget()

        lblErrorEmail = Label(marco5, text="", fg="red")
        lblErrorEmail.grid_forget()



        lblEliminar = Label(self.ventana, text="¡Presiona 'supr'!\¡nCon esto eliminaras al cliente seleccionado\ncon el mouse!")
        lblEliminar.grid(row=8, column=0, padx=5, pady=5)

        btnConsultarTodo=Button(self.ventana, text="Consulta los elementos", command=lambda:self.accion_consultar_todo(txtNombreCliente.get(), txtApellidoCliente.get(), txtCedulaCliente.get(), txtTelefonoCliente.get(), txtEmailCliente.get()))
        btnConsultarTodo.grid(row=9, column=0, padx=10, pady=10)

        self.tabla.tabla.grid(row=10, column=0, columnspan=3)

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicador.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        txtCedulaCliente.bind("<KeyRelease>", eventoVCedula)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)
        self.ventana.mainloop()
