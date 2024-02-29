from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkcalendar import *
from tkinter import ttk
import re

def obtener_fecha_nacimiento(): 
    def seleccionarFecha():
        fechaSelect = calendario.selection_get()
        entry_fecha_nacimiento.delete(0, "end")
        entry_fecha_nacimiento.insert(0, fechaSelect.strftime("%d-%m-%Y"))
        ventana_calendario.destroy()

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
    email=entry_email.get()
    fecha_nacimiento= entry_fecha_nacimiento.get()
    
    if not nombre or not apellido or not edad or not sexo or not email or not fecha_nacimiento:
        entry_nombre.config(state="disabled")
        entry_apellido.config(state="disabled")
        entry_edad.config(state="disabled")
        entry_sexo.config(state="disabled")
        entry_email.config(state="disabled")
        entry_fecha_nacimiento.config(state="disabled")
        messagebox.showerror("Error", "Complete todos los campos. Presione Click derecho")
        return


    if len(nombre) < 3 or len(apellido) < 4 or len(edad) < 0:
        messagebox.showerror("Error", "Para nombre y apellido se deben colocar al menos 4 caracteres, en la edad > 0")
        return


    if not re.match(r"^\d{2}-\d{2}-\d{4}$", fecha_nacimiento):
        messagebox.showerror("Error", "La fecha de nacimiento debe tener el formato DD-MM-AAAA.")
        return

#def Genero(event):
    if sexo not in ["H", "M", "Otro"]:
        messagebox.showerror("Error", "El género debe ser 'H', 'M', u 'Otro'.")
        return

def habilitarCampos(event):
    entry_nombre.config(state="normal")
    entry_apellido.config(state="normal")
    entry_edad.config(state="normal")
    entry_sexo.config(state="normal")
    entry_email.config(state="normal")
    entry_fecha_nacimiento.config(state="normal")
    messagebox.showinfo("Alerta", "Proceda a completarlos.")
    return


def validar_correo(event):
    correo = entry_email.get()
    if '@' not in correo:
        labelErrorEmail.config(text="Correo inválido", fg="red")
    else:
        labelErrorEmail.config(text="")


    

root = Tk()
root.title("Formulario")
frame = Frame(root)
frame.grid(row=0, column=0)
lblTitulo = LabelFrame(frame, text="Ingrese sus datos básicos")
lblTitulo.grid(row=0, column=0)

label_nombre = Label(frame, text="Nombre*:")
label_nombre.grid(row=0, column=0)
entry_nombre = Entry(frame)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

label_apellido = Label(frame, text="Apellido*:")
label_apellido.grid(row=1, column=0)
entry_apellido = Entry(frame)
entry_apellido.grid(row=1, column=1, padx=10, pady=10)

label_edad = Label(frame, text="Edad*:")
label_edad.grid(row=2, column=0)
entry_edad = Entry(frame)
entry_edad.grid(row=2, column=1, padx=10, pady=10)

label_email = Label(frame, text="E*mail*:")
label_email.grid(row=3, column=0)
entry_email = Entry(frame)
entry_email.grid(row=3, column=1, padx=10, pady=10)
labelErrorEmail= Label(frame, text="", fg="red")
labelErrorEmail.grid(row=3, column=2)

label_sexo = Label(frame, text="Sexo*:")
label_sexo.grid(row=4, column=0)
entry_sexo = ttk.Combobox(frame, values=[ "H", "M", "Otro"])
entry_sexo.grid(row=4, column=1, padx=10, pady=10)

label_fecha_nacimiento = Label(frame, text="Fecha de nacimiento*:")
label_fecha_nacimiento.grid(row=5, column=0, padx=10, pady=10)
entry_fecha_nacimiento = Entry(frame)
entry_fecha_nacimiento.insert(0, "dd-mm-yyyy")
entry_fecha_nacimiento.grid(row=5, column=1, padx=10, pady=10)
btnNacimiento = Button(frame, text="Inserta la fecha", command=obtener_fecha_nacimiento)
btnNacimiento.grid(row=5, column=2, padx=10, pady=10)


submit_button = Button(frame, text="Enviar")
submit_button.grid(row=6, columnspan=2, padx=10, pady=10)

root.bind('<Return>', Generardatos)
root.bind('<Button-3>', habilitarCampos)
entry_email.bind('<FocusOut>', validar_correo)

root.mainloop()
