from tkinter import *
from tkinter import ttk
import re
import requests
from modelos.usuario import Usuario
from tkinter import messagebox

def validarValoreventoVValor(valor):
    patronN = re.compile("^[A-Za-zñÑ ]*$")
    resultadoN = patronN.match(valor.get()) is not None
    if not resultadoN:
        return False
    return True

def eventoVValor(event):
    global ValoreventoVValor
    if validarValoreventoVValor(ValoreventoVValor):
        textoVValoreventoVValor=""
    else:
        textoVValoreventoVValor="ValoreventoVValor debe tener solo números"
    labelErrorValoreventoVValor.config(text=textoVValoreventoVValor)

def validarPeso(valorPeso):
    patronA = re.compile("^[A-Za-zñÑ ]*$")
    resultadoN = patronA.match(valorPeso.get()) is not None
    if not resultadoN:
        return False
    return True

def eventoVPeso(event):
    global Peso
    if validarPeso(Peso):
        textoVPeso=""
    else:
        textoVPeso="Peso debe tener solo números"
    labelErrorPeso.config(text=textoVPeso)

def validarTamañoeventoVTamaño(valor):
    patronA = re.compile(r"^\d{1}(\.\d{0,2})?$")
    resultadoN = patronA.match(valor) is not None
    if not resultadoN:
        return False
    return True

def eventoVTamaño(event):
    global TamañoeventoVTamaño
    valor_TamañoeventoVTamaño = txtAtr3.get() 
    if validarTamañoeventoVTamaño(valor_TamañoeventoVTamaño):
        textoVTamañoeventoVTamaño=""
    else:
        textoVTamañoeventoVTamaño="TamañoeventoVTamaño no cumple con lo establecido"
    lblErrorTamañoeventoVTamaño.config(text=textoVTamañoeventoVTamaño)

def validarColoreventoVColor(valor):
    patronA = re.compile(r"^\d{1,3}(\.\d{0,2})?$")
    resultadoN = patronA.match(valor) is not None
    if not resultadoN:
        return False
    return True

def eventoVColor(event):
    global ColoreventoVColor
    valorColoreventoVColor = txtAtr4.get() 
    if validarColoreventoVColor(valorColoreventoVColor):
        textoVColoreventoVColor=""
    else:
        textoVColoreventoVColor="ColoreventoVColor no cumple con lo establesido"
    lblErrorColoreventoVColor.config(text=textoVColoreventoVColor)


def validarInformacion():
        
    valorV = re.match(r"^[A-Za-zñÑ ]*$", usuario.valor.get())
    pesoV = re.match(r"^[A-Za-zñÑ ]*$", usuario.peso.get())
    tamañoV = re.match(r"^\d{1}(\.\d{0,2})?$", usuario.tamaño.get())
    colorV = re.match(r"^\d{1,3}(\.\d{0,2})?$", usuario.color.get())


    if valorV and pesoV and tamañoV and colorV:
                
        data = {
        "valor": usuario.valor.get(),
        "peso": usuario.peso.get(),
        "tamaño": usuario.tamaño.get(),
        "color": usuario.color.get()
                }
        respuesta = requests.post("http://127.0.0.1:8000/v1/Moneda", data)
        print(respuesta.status_code)
        print(respuesta.content)
                
        messagebox.showinfo("Información", "Se guardo correctamente")
    else:
        messagebox.showerror("Información", "No se pudo guardar, confirme si está correcto")


def validarInformacion():
    ValoreventoVValorV = re.match(r"^[A-Za-zñÑ ]*$", ValoreventoVValor.get())
    PesoV = re.match(r"^[A-Za-zñÑ ]*$", Peso.get())
    TamañoeventoVTamañoV = re.match(r"^\d{1}(\.\d{0,2})?$", TamañoeventoVTamaño.get())
    ColoreventoVColorV = re.match(r"^\d{1,3}(\.\d{0,2})?$", ColoreventoVColor.get())


    if ValoreventoVValorV and PesoV and TamañoeventoVTamañoV and ColoreventoVColorV:
        
        data = {
            "ValoreventoVValor": ValoreventoVValor.get(),
            "Peso": Peso.get(),
            "TamañoeventoVTamaño": TamañoeventoVTamaño.get(),
            "ColoreventoVColor": ColoreventoVColor.get()
        }
        respuesta = requests.post("http://127.0.0.1:8000/v1/moneda", data)
        print(respuesta.status_code)
        print(respuesta.content)
        
        messagebox.showinfo("Informacion", "Se guardo correctamente")
    else:
        messagebox.showerror("Informacion", "No se pudo guardar, confirme si está correcto")

root=Tk()
root.title("Clase moneda")
root.resizable(0,0)
usuario=Usuario(root)
ValoreventoVValor=StringVar(root)
Peso=StringVar(root)
TamañoeventoVTamaño=StringVar(root)
ColoreventoVColor=StringVar(root)

marcotitulo=LabelFrame(root)
marcotitulo.grid(row=0, column=1, padx=5, pady=5)

lblTitulo=Label(marcotitulo, text="Clase-moneda")
lblTitulo.grid(row=0, column=0, padx=10, pady=10)

marcoAtr1=LabelFrame(root)
marcoAtr1.grid(row=1, column=0, padx=5, pady=5)

lblAtr1=Label(marcoAtr1, text="Ingrese el valor de la moneda*\nTenga en cuenta que solo son números, sin caracteres especiales o letras")
lblAtr1.grid(row=0, column=0)
txtAtr1=Entry(marcoAtr1, textvariable=ValoreventoVValor)
txtAtr1.grid(row=0,column=1, padx=10, pady=10)
labelErrorValoreventoVValor=Label(marcoAtr1, text="", fg="red")
labelErrorValoreventoVValor.grid(row=1, column=1)

marcoAtr2=LabelFrame(root)
marcoAtr2.grid(row=2, column=0, padx=5, pady=5)

lblAtr2=Label(marcoAtr2, text="Ingrese el peso de la moneda(en kg)*\nTenga en cuenta que solo son números, sin caracteres especiales o letras")
lblAtr2.grid(row=0,column=0)
txtAtr2=Entry(marcoAtr2, textvariable=Peso)
txtAtr2.grid(row=0, column=1, padx=10, pady=10)
labelErrorPeso=Label(marcoAtr2, text="", fg="red")
labelErrorPeso.grid(row=1, column=1)

marcoAtr3=LabelFrame(root)
marcoAtr3.grid(row=1, column=2, padx=5, pady=5)

lblAtr3=Label(marcoAtr3, text="Ingrese el tamaño de la moneda*")
lblAtr3.grid(row=0,column=0)
txtAtr3=Entry(marcoAtr3, textvariable=TamañoeventoVTamaño)
txtAtr3.grid(row=0, column=1, padx=10, pady=10)
lblErrorTamañoeventoVTamaño=Label(marcoAtr3, text="", fg="red")
lblErrorTamañoeventoVTamaño.grid(row=1, column=1)

marcoAtr4=LabelFrame(root)
marcoAtr4.grid(row=2,column=2, padx=5, pady=5)

lblAtr4=Label(marcoAtr4, text="Ingrese el color de la moneda*\nSolo son colores")
lblAtr4.grid(row=0,column=0)
txtAtr4=Entry(marcoAtr4, textvariable=ColoreventoVColor)
txtAtr4.grid(row=0, column=1, padx=10, pady=10)
lblErrorColoreventoVColor=Label(marcoAtr4, text="", fg="red")
lblErrorColoreventoVColor.grid(row=1, column=1)
btnGuardar=Button(root, text="Guardar", padx=10, pady=10, command=validarInformacion)
btnGuardar.grid(row=3, column=1, padx=10, pady=10)


txtAtr1.bind("<KeyRelease>", eventoVValor)
txtAtr2.bind("<KeyRelease>", eventoVPeso)
txtAtr3.bind("<KeyRelease>", eventoVTamaño)
txtAtr4.bind("<KeyRelease>", eventoVColor)

root.mainloop()