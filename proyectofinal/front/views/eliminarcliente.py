from tkinter import *
import tkinter as tk
from models.modelos import Cliente
from controler.controlador import Validaciones
from .tabla import Tabla
from controler.comunicador import Comunicacion
from tkinter import messagebox

class EliminarCliente:
    def __init__(self, menuSecundario):
        titulos = ['Identificador', 'Nombre', 'Apellido', 'Cédula', 'Teléfono', 'Email']
        columnas = ['id', 'nombre', 'apellido', 'cedula', 'telefono', 'email']
        data = []
        self.ventana = tk.Toplevel(menuSecundario)
        self.comunicador = Comunicacion(self.ventana)
        self.tabla = Tabla(self.ventana, titulos, columnas, data)
        self.cargar_tabla()
    
    def cargar_tabla(self):
        resultado = self.comunicador.consultar_todo('', '', '', '','')
        data = []
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('nombre'), elemento.get('apellido'), elemento.get('cedula'), elemento.get('telefono'), elemento.get('email')))
        self.tabla.refrescar(data)


    def mostrarInterfaz(self):

        self.ventana.focus_set()
        self.ventana.title("Eliminar Cliente")
        self.ventana.resizable(0, 0)
        cliente = Cliente(self.ventana)

        # Marco del título
        marcoTitulo = LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=1, padx=10, pady=10)
        lblTitulo = Label(marcoTitulo, text="Eliminar Cliente")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        

        lblEliminar = Label(self.ventana, text="¡Presiona 'supr'!\n¡Con esto eliminaras al cliente seleccionado\ncon el mouse!")
        lblEliminar.grid(row=8, column=1, padx=5, pady=5)

        self.tabla.tabla.grid(row=10, column=0, columnspan=3)

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicador.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)
                messagebox.showinfo("Informa","Se eliminó el cliente")

        self.tabla.tabla.bind('<Delete>', borrar_elemento)
        self.ventana.mainloop()
