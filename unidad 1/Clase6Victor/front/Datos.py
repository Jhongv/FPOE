from tkinter import *
from tkinter import ttk
import re
import requests
from tkinter import messagebox

def validarNombre(valor):
    patronN = re.compile("^[A-Za-zñÑ ]*$")
    resultadoN = patronN.match(valor.get()) is not None
    if not resultadoN:
        return False
    return True

def eventoVnombre(event):
    global nombre
    if validarNombre(nombre):
        textoVnombre=""
    else:
        textoVnombre="Nombre debe tener solo letras"
    labelErrorNombre.config(text=textoVnombre)

def validarApellido(valorApellido):
    patronA = re.compile("^[A-Za-zñÑ ]*$")
    resultadoN = patronA.match(valorApellido.get()) is not None
    if not resultadoN:
        return False
    return True

def eventoVApellido(event):
    global apellido
    if validarApellido(apellido):
        textoVapellido=""
    else:
        textoVapellido="Apellido debe tener solo letras"
    labelErrorApellido.config(text=textoVapellido)

def validarEstatura(valor):
    patronA = re.compile(r"^\d{1,2}(\.\d{0,2})?$")
    resultadoN = patronA.match(valor) is not None
    if not resultadoN:
        return False
    return True

def eventoVEstatura(event):
    global estatura
    valor_estatura = estatura.get()
    if not valor_estatura.replace('.', ''):
        textoVEstatura = "Por favor, ingrese solo números y un punto para los decimales"
    elif validarEstatura(valor_estatura):
        textoVEstatura=""
    else:
        textoVEstatura="Estatura no cumple con lo establecido"
    lblErrorEstatura.config(text=textoVEstatura)

def validarPeso(valor):
    patronA = re.compile(r"^\d{1,2}(\.\d{0,2})?$")
    resultadoN = patronA.match(valor) is not None
    if not resultadoN:
        return False
    return True

def eventoVPeso(event):
    global peso
    valorPeso = peso.get() 
    if not valorPeso.replace('.', ''):
        textoVpeso = "Por favor, ingrese solo números y un punto para los decimales"
    elif validarPeso(valorPeso):
        textoVpeso=""
    else:
        textoVpeso="Peso no cumple con lo establecido"
    lblErrorPeso.config(text=textoVpeso)

def validarInformacion():
    nombreV = re.match(r"^[A-Za-zñÑ ]*$", nombre.get())
    apellidoV = re.match(r"^[A-Za-zñÑ ]*$", apellido.get())
    estaturaV = re.match(r"^\d{1,2}(\.\d{0,2})?$", estatura.get()).group()
    pesoV = re.match(r"^\d{1,2}(\.\d{0,2})?$", peso.get()).group()


    if nombreV and apellidoV and estaturaV and pesoV:
        
        data = {
            "nombre": nombre.get(),
            "apellido": apellido.get(),
            "estatura": estatura.get(),
            "peso": peso.get()
        }
        respuesta = requests.post("http://127.0.0.1:8000/v1/persona", data)
        print(respuesta.status_code)
        print(respuesta.content)
        
        messagebox.showinfo("Informacion", "Se guardo correctamente")
    else:
        messagebox.showerror("Informacion", "No se pudo guardar, confirme si está correcto")

root=Tk()
root.title("Clase persona")
root.resizable(0,0)
nombre=StringVar(root)
apellido=StringVar(root)
estatura=StringVar(root)
peso=StringVar(root)

marcotitulo=LabelFrame(root)
marcotitulo.grid(row=0, column=1, padx=5, pady=5)

lblTitulo=Label(marcotitulo, text="Clase-Persona")
lblTitulo.grid(row=0, column=0, padx=10, pady=10)

marcoAtr1=LabelFrame(root)
marcoAtr1.grid(row=1, column=0, padx=5, pady=5)

lblAtr1=Label(marcoAtr1, text="Ingrese el 1er atributo de Cl/Persona(Nombre)*:")
lblAtr1.grid(row=0, column=0)
txtAtr1=Entry(marcoAtr1, textvariable=nombre)
txtAtr1.grid(row=0,column=1, padx=10, pady=10)
labelErrorNombre=Label(marcoAtr1, text="", fg="red")
labelErrorNombre.grid(row=1, column=1)

marcoAtr2=LabelFrame(root)
marcoAtr2.grid(row=2, column=0, padx=5, pady=5)

lblAtr2=Label(marcoAtr2, text="Ingrese el 2do atributo de Cl/Persona(Apellido)*:")
lblAtr2.grid(row=0,column=0)
txtAtr2=Entry(marcoAtr2, textvariable=apellido)
txtAtr2.grid(row=0, column=1, padx=10, pady=10)
labelErrorApellido=Label(marcoAtr2, text="", fg="red")
labelErrorApellido.grid(row=1, column=1)

marcoAtr3=LabelFrame(root)
marcoAtr3.grid(row=1, column=2, padx=5, pady=5)

lblAtr3=Label(marcoAtr3, text="Ingrese el 3er atributo de Cl/Persona(Estatura(Cm)/float)*:")
lblAtr3.grid(row=0,column=0)
txtAtr3=Entry(marcoAtr3, textvariable=estatura)
txtAtr3.grid(row=0, column=1, padx=10, pady=10)
lblErrorEstatura=Label(marcoAtr3, text="", fg="red")
lblErrorEstatura.grid(row=1, column=1)

marcoAtr4=LabelFrame(root)
marcoAtr4.grid(row=2,column=2, padx=5, pady=5)

lblAtr4=Label(marcoAtr4, text="Ingrese el 4to atributo de Cl/Persona(Peso(Kg)/int)*:")
lblAtr4.grid(row=0,column=0)
txtAtr4=Entry(marcoAtr4, textvariable=peso)
txtAtr4.grid(row=0, column=1, padx=10, pady=10)
lblErrorPeso=Label(marcoAtr4, text="", fg="red")
lblErrorPeso.grid(row=1, column=1)
btnGuardar=Button(root, text="Guardar", padx=10, pady=10)
btnGuardar.grid(row=3, column=1, padx=10, pady=10)


txtAtr1.bind("<KeyRelease>", eventoVnombre)
txtAtr2.bind("<KeyRelease>", eventoVApellido)
txtAtr3.bind("<KeyRelease>", eventoVEstatura)
txtAtr4.bind("<KeyRelease>", eventoVPeso)

root.mainloop()