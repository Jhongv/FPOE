from tkinter import *
import tkinter as tk
from tkinter import ttk
class ActualizarCliente():

    def __init__(self, menuSecundario):
        self.ventana=tk.Toplevel(menuSecundario)


    def selectCombobox(self, event, combobox, lblNombre, txtNombre):
        select=combobox.get()
        if select == "Nombre":
            lblNombre.grid(row=0, column=0)
            txtNombre.grid(row=0, column=1)

        else:
            lblNombre.grid_forget()
            txtNombre.grid_forget()


    #Marco del titulo
    def mostrarInterfaz(self):

        self.ventana.focus_set()
        self.ventana.title("Actualizar al cliente")
        self.ventana.resizable(0,0)


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

        txtNombreCliente=Entry(marco2)
        txtNombreCliente.grid_forget()

        
        cbxSeleccionarCampoActualizar.bind("<<ComboboxSelected>>", lambda event: self.selectCombobox(event, cbxSeleccionarCampoActualizar, lblNombreCliente, txtNombreCliente))
        
        


        self.ventana.mainloop()