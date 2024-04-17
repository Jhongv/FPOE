from tkinter import *
from tkinter import ttk
import re
import requests
from tkinter import messagebox

def validarValor(valor):
    patronN = re.compile("^[5-9]\d{1,2}$|^[1-9]\d{3}$")
    resultadoN = patronN.match(valor.get()) is not None
    if not resultadoN:
        return False
    return True

def eventoVValor(event):
    global valor
    if validarValor(valor):
        textoVValor=""
    else:
        textoVValor="Valor solo debe tener números"
    labelErrorValor.config(text=textoVValor)


def validarPeso(valorpeso):
    patronA = re.compile(r"^\d{1,3}(\.\d{0,2})?$")
    resultadoN = patronA.match(valorpeso)
    return resultadoN is not None

def eventoVPeso(event):
    global peso
    valorPeso = txtAtr2.get()

    if validarPeso(valorPeso):
        textoVpeso = ""
    else:
        textoVpeso = "Peso debe tener solo números"
    labelErrorPeso.config(text=textoVpeso)


def validarTamaño(valor):
    patronA = re.compile(r"^\d{1,2}(\.\d{0,2})?$")
    resultadoN = patronA.match(valor) is not None
    if not resultadoN:
        return False
    return True

def eventoVTamaño(event):
    global tamaño
    valor_tamaño = txtAtr3.get() 
    if validarTamaño(valor_tamaño):
        textoVTamaño=""
    else:
        textoVTamaño="tamaño no cumple con lo establesido"
    lblErrorTamaño.config(text=textoVTamaño)

def validarcolor(valor):
    patronA = re.compile("^[A-Za-zñÑ ]*$")
    resultadoN = patronA.match(valor.get()) is not None
    if not resultadoN:
        return False
    return True

def eventoVColor(event):
    global color
    if validarcolor(color):
        textoVcolor=""
    else:
        textoVcolor="Tiene que ser un color válido"
    lblErrorcolor.config(text=textoVcolor)

def validarInformacion():
    valorV = re.match(r"^[5-9]\d{1,2}$|^[1-9]\d{3}$", valor.get())
    pesoV = re.match(r"^\d{1,3}(\.\d{0,2})?$", peso.get())
    tamañoV = re.match(r"^\d{1,2}(\.\d{0,2})?$", tamaño.get())
    colorV = re.match(r"^[A-Za-zñÑ ]*$", color.get())


    if valorV and pesoV and tamañoV and colorV:
        
        data = {
            "valor": valor.get(),
            "peso": peso.get(),
            "tamaño": tamaño.get(),
            "color": color.get()
        }
        respuesta = requests.post("http://127.0.0.1:8000/v1/moneda", data)
        print(respuesta.status_code)
        print(respuesta.content)
        
        messagebox.showinfo("Información", "Guardado correctamente")
    else:
        messagebox.showerror("Información", "No se pudo guardar, confirme si está correcto")

root=Tk()
root.title("Clase moneda")
root.resizable(0,0)
valor=StringVar(root)
peso=StringVar(root)
tamaño=StringVar(root)
color=StringVar(root)

marcotitulo=LabelFrame(root)
marcotitulo.grid(row=0, column=1, padx=5, pady=5)

lblTitulo=Label(marcotitulo, text="Clase - Moneda")
lblTitulo.grid(row=0, column=0, padx=10, pady=10)

marcoAtr1=LabelFrame(root)
marcoAtr1.grid(row=1, column=0, padx=5, pady=5)

lblAtr1=Label(marcoAtr1, text="Ingrese el 1er atributo de Cl/Moneda(Valor)*\nTenga en cuenta que solo son números, sin caracteres especiales o letras:")
lblAtr1.grid(row=0, column=0)
txtAtr1=Entry(marcoAtr1, textvariable=valor)
txtAtr1.grid(row=0,column=1, padx=10, pady=10)
labelErrorValor=Label(marcoAtr1, text="", fg="red")
labelErrorValor.grid(row=1, column=1)

marcoAtr2=LabelFrame(root)
marcoAtr2.grid(row=2, column=0, padx=5, pady=5)

lblAtr2=Label(marcoAtr2, text="Ingrese el 2do atributo de Cl/Moneda(Peso)*\nTenga en cuenta que solo son números, sin caracteres especiales o letras:")
lblAtr2.grid(row=0,column=0)
txtAtr2=Entry(marcoAtr2, textvariable=peso)
txtAtr2.grid(row=0, column=1, padx=10, pady=10)
labelErrorPeso=Label(marcoAtr2, text="", fg="red")
labelErrorPeso.grid(row=1, column=1)

marcoAtr3=LabelFrame(root)
marcoAtr3.grid(row=1, column=2, padx=5, pady=5)

lblAtr3=Label(marcoAtr3, text="Ingrese el 3er atributo de Cl/Moneda(tamaño(centímetros)/Decimal)\nTenga en cuenta esta forma de inserción\nd--> dígito; 1d unico antes del punto y max 2d después de este:")
lblAtr3.grid(row=0,column=0)
txtAtr3=Entry(marcoAtr3, textvariable=tamaño)
txtAtr3.grid(row=0, column=1, padx=10, pady=10)
lblErrorTamaño=Label(marcoAtr3, text="", fg="red")
lblErrorTamaño.grid(row=1, column=1)

marcoAtr4=LabelFrame(root)
marcoAtr4.grid(row=2,column=2, padx=5, pady=5)

lblAtr4=Label(marcoAtr4, text="Ingrese el 4to atributo de Cl/Moneda*\nTenga en cuenta que solo son colores: ")
lblAtr4.grid(row=0,column=0)
txtAtr4=Entry(marcoAtr4, textvariable=color)
txtAtr4.grid(row=0, column=1, padx=10, pady=10)
lblErrorcolor=Label(marcoAtr4, text="", fg="red")
lblErrorcolor.grid(row=1, column=1)
btnGuardar=Button(root, text="Guardar", padx=10, pady=10, command=validarInformacion)
btnGuardar.grid(row=3, column=1, padx=10, pady=10)


txtAtr1.bind("<KeyRelease>", eventoVValor)
txtAtr2.bind("<KeyRelease>", eventoVPeso)
txtAtr3.bind("<KeyRelease>", eventoVTamaño)
txtAtr4.bind("<KeyRelease>", eventoVColor)

root.mainloop()

