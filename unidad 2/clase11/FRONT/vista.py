from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controlador.controlador import ControladorMoneda

class VistaMoneda:
    def __init__(self, root):
        self.root = root
        self.root.title("Clase moneda")
        self.root.resizable(0,0)
        
        self.valor = StringVar(root)
        self.peso = StringVar(root)
        self.tamaño = StringVar(root)
        self.color = StringVar(root)
        
        self.controlador = ControladorMoneda(self)
        self.crear_interfaz()

    def crear_interfaz(self):
        self.marcotitulo = LabelFrame(self.root)
        self.marcotitulo.grid(row=0, column=1, padx=5, pady=5)

        self.lblTitulo = Label(self.marcotitulo, text="Clase - Moneda")
        self.lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        self.marcoAtr1 = LabelFrame(self.root)
        self.marcoAtr1.grid(row=1, column=0, padx=5, pady=5)

        self.lblAtr1 = Label(self.marcoAtr1, text="Ingrese el valor de la moneda*\nTenga en cuenta que solo son números, sin caracteres especiales o letras:")
        self.lblAtr1.grid(row=0, column=0)
        self.txtAtr1 = Entry(self.marcoAtr1, textvariable=self.valor)
        self.txtAtr1.grid(row=0,column=1, padx=10, pady=10)
        self.labelErrorValor = Label(self.marcoAtr1, text="", fg="red")
        self.labelErrorValor.grid(row=1, column=1)

        self.marcoAtr2 = LabelFrame(self.root)
        self.marcoAtr2.grid(row=2, column=0, padx=5, pady=5)

        self.lblAtr2 = Label(self.marcoAtr2, text="Ingrese el peso de la moneda*\nTenga en cuenta que solo son números, sin caracteres especiales o letras:")
        self.lblAtr2.grid(row=0,column=0)
        self.txtAtr2 = Entry(self.marcoAtr2, textvariable=self.peso)
        self.txtAtr2.grid(row=0, column=1, padx=10, pady=10)
        self.labelErrorPeso = Label(self.marcoAtr2, text="", fg="red")
        self.labelErrorPeso.grid(row=1, column=1)

        self.marcoAtr3 = LabelFrame(self.root)
        self.marcoAtr3.grid(row=1, column=2, padx=5, pady=5)

        self.lblAtr3 = Label(self.marcoAtr3, text="Ingrese el tamaño de la moneda \n(En centímetros):")
        self.lblAtr3.grid(row=0,column=0)
        self.txtAtr3 = Entry(self.marcoAtr3, textvariable=self.tamaño)
        self.txtAtr3.grid(row=0, column=1, padx=10, pady=10)
        self.lblErrorTamaño = Label(self.marcoAtr3, text="", fg="red")
        self.lblErrorTamaño.grid(row=1, column=1)

        self.marcoAtr4 = LabelFrame(self.root)
        self.marcoAtr4.grid(row=2,column=2, padx=5, pady=5)

        self.lblAtr4 = Label(self.marcoAtr4, text="Ingrese el color de la moneda\nTenga en cuenta que solo son colores: ")
        self.lblAtr4.grid(row=0,column=0)
        self.txtAtr4 = Entry(self.marcoAtr4, textvariable=self.color)
        self.txtAtr4.grid(row=0, column=1, padx=10, pady=10)
        self.lblErrorcolor = Label(self.marcoAtr4, text="", fg="red")
        self.lblErrorcolor.grid(row=1, column=1)

        self.btnGuardar = Button(self.root, text="Guardar", padx=10, pady=10, command=self.controlador.validarInformacion)
        self.btnGuardar.grid(row=3, column=1, padx=10, pady=10)

        self.txtAtr1.bind("<KeyRelease>", self.controlador.eventoVValor)
        self.txtAtr2.bind("<KeyRelease>", self.controlador.eventoVPeso)
        self.txtAtr3.bind("<KeyRelease>", self.controlador.eventoVTamaño)
        self.txtAtr4.bind("<KeyRelease>", self.controlador.eventoVColor)

def iniciar_aplicacion():
    root = Tk()
    vista_moneda = VistaMoneda(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()

