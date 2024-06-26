from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkcalendar import *
from tkinter import ttk
import re

textoVemail = ""

textoVnombre = ""
textoVApellido = ""
textoVEdad = ""

def obtener_fecha_nacimiento(): 
    def seleccionarFecha():
        fechaSelect = calendario.selection_get()
        entry_fecha_nacimiento.delete(0, "end")
        entry_fecha_nacimiento.insert(0, fechaSelect.strftime("%d-%m-%Y"))
        ventana_calendario.destroy()
        return fechaSelect

    ventana_calendario = Toplevel(root) 
    ventana_calendario.title("Seleccionar Fecha de Nacimiento")
    calendario = Calendar(ventana_calendario, year=2000, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy")
    calendario.pack(pady=10)

    btnSelect = Button(ventana_calendario, text="Seleccionar", command=seleccionarFecha)
    btnSelect.pack(pady=10)

def Generardatos(event):
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    sexo = entry_sexo.get()
    email = entry_email.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()


    if not nombre or not apellido or not edad or not sexo or not email or not fecha_nacimiento:
        entry_nombre.config(state="disabled")
        entry_apellido.config(state="disabled")
        entry_edad.config(state="disabled")
        entry_sexo.config(state="disabled")
        entry_email.config(state="disabled")
        entry_fecha_nacimiento.config(state="disabled")
        labelErrorNombre.config(text="Complete todos los campos", fg="red")
        return
    else:
        labelErrorNombre.config(text="")


    ventanaDeLosdatos = Toplevel()
    ventanaDeLosdatos.title("Sus datos")
    ventanaDeLosdatos.geometry("300x300")
    lblFrame = LabelFrame(ventanaDeLosdatos, text="Mira")
    lblFrame.grid(row=0, column=0, padx=10, pady=10)
    lblNombre = Label(lblFrame, text=nombre)
    lblNombre.grid(row=1, column=0, padx=10, pady=10)
    lblApellido = Label(lblFrame, text=apellido)
    lblApellido.grid(row=2, column=0, padx=10, pady=10)
    lblSexo = Label(lblFrame, text=sexo)
    lblSexo.grid(row=3, column=0, padx=10, pady=10)
    lblEmail = Label(lblFrame, text=email)
    lblEmail.grid(row=4, column=0, padx=10, pady=10)
    lblFN = Label(lblFrame, text=fecha_nacimiento)
    lblFN.grid(row=5, column=0, padx=10, pady=10)
    
def generarFecha(event):
    global fecha_nacimiento
    if fecha_nacimiento:
        textoVFN=""
        entry_fecha_nacimiento.delete(0, "end")
    else:
        textoVFN="Esta mal fecha de nacimiento dd-mm-yyyy"
    labelErrorFecha.config(text=textoVFN)
        

def Genero(event):
    sexo = entry_sexo.get()
    if sexo not in ["H", "M", "Otro"]:
        labelErrorSexo.config(text="Géneros permitidos: H o M u Otro")
        entry_sexo.delete(0, "end")
    else:
        labelErrorSexo.config(text="")

def habilitarCampos(event):
    entry_nombre.config(state="normal")
    entry_apellido.config(state="normal")
    entry_edad.config(state="normal")
    entry_sexo.config(state="normal")
    entry_email.config(state="normal")
    entry_fecha_nacimiento.config(state="normal")
    messagebox.showinfo("Alerta", "Proceda a completarlos.")

def validarCorreo(valor):
    patronC = r"^[a-zA-Z0-9._%+-]+@(gmail\.com|hotmail\.com|yahoo\.com)$"
    return re.fullmatch(patronC, valor) is not None

def generarCorreo(event):
    global textoVemail
    email_valor = entry_email.get()
    if validarCorreo(email_valor):
        textoVemail = ""
    else:
        textoVemail = "Solo es permitido @ seguido de gmail.com, yahoo.com o hotmail.com"
    labelErrorEmail.config(text=textoVemail)

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
    patronA= re.compile("^[A-Za-zñÑ ]*$")
    resultadoA = patronA.match(valorApellido.get()) is not None
    if not resultadoA:
        return False
    return True 

def eventoVApellido(event):
    global apellido
    if validarApellido(apellido):
        textoVApellido=""
    else:
        textoVApellido="Apellido debe tener solo letras"
    labelErrorApellido.config(text=textoVApellido)

def validar_edad():
    try:
        edad = int(entry_edad.get())
        if edad < 0 or edad > 120:  # Establecer un rango aceptable para la edad (por ejemplo, entre 0 y 120 años)
            labelErrorEdad.config(text="La edad debe estar entre 0 y 120 años", fg="red")
            return False
        else:
            labelErrorEdad.config(text="")
            return True
    except ValueError:
        labelErrorEdad.config(text="Por favor, ingrese un número entero válido para la edad", fg="red")
        return False

def eventoVEdad(event):
    validar_edad()


def validarApellido(valorApellido):
    patronA= re.compile("^[A-Za-zñÑ ]*$")
    resultadoA = patronA.match(valorApellido.get()) is not None
    if not resultadoA:
        return False
    return True 

def eventoVApellido(event):
    global apellido
    if validarApellido(apellido):
        textoVApellido=""
    else:
        textoVApellido="Apellido debe tener solo letras"
    labelErrorApellido.config(text=textoVApellido)

def eventoVEdad(event):
    validar_edad()


root = Tk()
root.title("Formulario")
root.resizable(False, False)

frame = Frame(root)
frame.grid(row=0, column=0)
nombre=StringVar(frame)
apellido=StringVar(frame)

edad=IntVar()

edad=IntVar(frame)

lblTitulo = LabelFrame(frame, text="Ingrese sus datos básicos")
lblTitulo.grid(row=0, column=0)


label_nombre = Label(frame, text="Nombre*:")
label_nombre.grid(row=0, column=0)
entry_nombre = Entry(frame, textvariable=nombre)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)
labelErrorNombre=Label(frame, text="", fg="red")
labelErrorNombre.grid(row=0, column=2)



label_apellido = Label(frame, text="Apellido*:")
label_apellido.grid(row=1, column=0)
entry_apellido = Entry(frame, textvariable=apellido)
entry_apellido.grid(row=1, column=1, padx=10, pady=10)
labelErrorApellido=Label(frame, text="", fg="red")
labelErrorApellido.grid(row=1, column=2)

label_edad = Label(frame, text="Edad*:")
label_edad.grid(row=2, column=0)
entry_edad = Entry(frame)
entry_edad.grid(row=2, column=1, padx=10, pady=10)
labelErrorEdad = Label(frame, text="", fg="red")
labelErrorEdad.grid(row=2, column=2)

label_email = Label(frame, text="E-mail*:")
label_email.grid(row=3, column=0)
entry_email = Entry(frame)
entry_email.grid(row=3, column=1, padx=10, pady=10)
labelErrorEmail = Label(frame, text="", fg="red")
labelErrorEmail.grid(row=3, column=2)

label_sexo = Label(frame, text="Sexo*:")
label_sexo.grid(row=4, column=0)
entry_sexo = ttk.Combobox(frame, values=["H", "M", "Otro"])
entry_sexo.grid(row=4, column=1, padx=10, pady=10)
labelErrorSexo = Label(frame, text="", fg="red")
labelErrorSexo.grid(row=4, column=2)

label_fecha_nacimiento = Label(frame, text="Fecha de nacimiento*:")
label_fecha_nacimiento.grid(row=5, column=0, padx=10, pady=10)
entry_fecha_nacimiento = Entry(frame)
entry_fecha_nacimiento.insert(0, "dd-mm-yyyy")
entry_fecha_nacimiento.grid(row=5, column=1, padx=10, pady=10)
btnNacimiento = Button(frame, text="Inserta la fecha", command=obtener_fecha_nacimiento)
btnNacimiento.grid(row=5, column=2, padx=10, pady=10)

labelErrorFecha = Label(frame, text="", fg="red")
labelErrorFecha.grid(row=6, column=1)

labelEnter=Label(frame, text="ENTER para ver sus datos")
labelEnter.grid(row=7, column=1, pady=10)

root.bind('<Return>', Generardatos)
root.bind('<Button-3>', habilitarCampos)
entry_email.bind('<KeyRelease>', generarCorreo)
entry_nombre.bind('<KeyRelease>', eventoVnombre)
entry_apellido.bind('<KeyRelease>', eventoVApellido)



entry_edad.bind('<KeyRelease>', eventoVEdad)

entry_fecha_nacimiento.bind('<FocusOut>', generarFecha)
entry_sexo.bind('<FocusOut>', Genero)
entry_edad.bind('<KeyRelease>', eventoVEdad)


root.mainloop()


