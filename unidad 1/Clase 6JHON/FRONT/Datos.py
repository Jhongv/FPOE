from tkinter import *
import re
import requests
from tkinter import messagebox

def validarMarca(marca):
    patron = re.compile(r"^[a-zA-Z]+$")
    return patron.match(marca)

def eventoVMarca(event):
    global marca
    if not validarMarca(marca.get()):
        labelErrorMarca.config(text="Solo debe contener letras")
    else:
        labelErrorMarca.config(text="")

def validarTalla(talla):
    patron = re.compile(r"^\d{1,3}(\.\d{0,2})?$")
    return patron.match(talla)

def eventoVTalla(event):
    global talla
    if not validarTalla(talla.get()):
        labelErrorTalla.config(text="Talla debe contener solo números")
    else:
        labelErrorTalla.config(text="")

def validarComponentes(componentes):
    patron = re.compile(r"^[\w\s-]{1,50}$")
    return patron.match(componentes)

def eventoVComponentes(event):
    global componentes
    if not validarComponentes(componentes.get()):
        lblErrorComponentes.config(text="El formato de componentes no es válido")
    else:
        lblErrorComponentes.config(text="")

def validarValor(valor):
    patron = re.compile(r"^\d+$")
    return patron.match(valor)

def eventoVValor(event):
    global valor
    if not validarValor(valor.get()):
        lblErrorValor.config(text="El valor debe ser un número entero")
    else:
        lblErrorValor.config(text="")

def validarInformacion():
    if validarMarca(marca.get()) and validarTalla(talla.get()) and validarComponentes(componentes.get()) and validarValor(valor.get()):
        data = {
            "marca": marca.get(),
            "talla": talla.get(),
            "componentes": componentes.get(),
            "valor": valor.get()
        }
        # Realizar la solicitud POST aquí
        messagebox.showinfo("Información", "Guardado correctamente")
    else:
        messagebox.showerror("Información", "Por favor, ingrese valores válidos")

root=Tk()
root.title("Clase cicla")
root.resizable(0,0)

marca = StringVar()
talla = StringVar()
componentes = StringVar()
valor = StringVar()

marcotitulo=LabelFrame(root)
marcotitulo.grid(row=0, column=1, padx=5, pady=5)

lblTitulo=Label(marcotitulo, text="Clase - Cicla")
lblTitulo.grid(row=0, column=0, padx=10, pady=10)

marcoAtr1=LabelFrame(root)
marcoAtr1.grid(row=1, column=0, padx=5, pady=5)

lblAtr1=Label(marcoAtr1, text="Marca*")
lblAtr1.grid(row=0, column=0)
txtAtr1=Entry(marcoAtr1, textvariable=marca)
txtAtr1.grid(row=0,column=1, padx=10, pady=10)
labelErrorMarca=Label(marcoAtr1, text="", fg="red")
labelErrorMarca.grid(row=1, column=1)

marcoAtr2=LabelFrame(root)
marcoAtr2.grid(row=2, column=0, padx=5, pady=5)

lblAtr2=Label(marcoAtr2, text="Talla*")
lblAtr2.grid(row=0,column=0)
txtAtr2=Entry(marcoAtr2, textvariable=talla)
txtAtr2.grid(row=0, column=1, padx=10, pady=10)
labelErrorTalla=Label(marcoAtr2, text="", fg="red")
labelErrorTalla.grid(row=1, column=1)

marcoAtr3=LabelFrame(root)
marcoAtr3.grid(row=1, column=2, padx=5, pady=5)

lblAtr3=Label(marcoAtr3, text="Componentes*")
lblAtr3.grid(row=0,column=0)
txtAtr3=Entry(marcoAtr3, textvariable=componentes)
txtAtr3.grid(row=0, column=1, padx=10, pady=10)
lblErrorComponentes=Label(marcoAtr3, text="", fg="red")
lblErrorComponentes.grid(row=1, column=1)

marcoAtr4=LabelFrame(root)
marcoAtr4.grid(row=2,column=2, padx=5, pady=5)

lblAtr4=Label(marcoAtr4, text="Valor*")
lblAtr4.grid(row=0,column=0)
txtAtr4=Entry(marcoAtr4, textvariable=valor)
txtAtr4.grid(row=0, column=1, padx=10, pady=10)
lblErrorValor=Label(marcoAtr4, text="", fg="red")
lblErrorValor.grid(row=1, column=1)

btnGuardar=Button(root, text="Guardar", padx=10, pady=10, command=validarInformacion)
btnGuardar.grid(row=3, column=1, padx=10, pady=10)

txtAtr1.bind("<KeyRelease>", eventoVMarca)
txtAtr2.bind("<KeyRelease>", eventoVTalla)
txtAtr3.bind("<KeyRelease>", eventoVComponentes)
txtAtr4.bind("<KeyRelease>", eventoVValor)

root.mainloop()
