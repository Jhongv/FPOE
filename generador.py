from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkcalendar import *

def submit():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    sexo = entry_sexo.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()


    mensaje = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nSexo: {sexo}\nFecha de nacimiento: {fecha_nacimiento}"
    messagebox.showinfo("Información ingresada", mensaje)


def obtener_fecha_nacimiento():
    def seleccionarFecha():
        fechaSelect=calendario.selection_get()
        entry_fecha_nacimiento.delete(0, "end")
        entry_fecha_nacimiento.insert(0,fechaSelect.strftime("%d-%m-%Y"))
        ventana_calendario.destroy()

    ventana_calendario =Toplevel(root) #Creamos la ventana donde se verá el calendario
    ventana_calendario.title("Seleccionar Fecha de Nacimiento")
    calendario=Calendar(ventana_calendario, year=2000, background="darkblue", foreground="white", date_pattern="dd-mm-yyyy")#Creamos el calendario
    calendario.pack(pady=10)

    btnSelect=Button(ventana_calendario, text="Seleccionar", command=seleccionarFecha)
    btnSelect.pack(pady=10)
    

root = Tk()
root.title("Formulario")
frame=Frame(root)
frame.grid(row=0, column=0)
lblTitulo=LabelFrame(frame, text="Ingrese sus datos básicos")
lblTitulo.grid(row=0, column=0)
label_nombre = Label(frame, text="Nombre:")
entry_nombre = Entry(frame)

label_apellido = Label(frame, text="Apellido:")
entry_apellido = Entry(frame)

label_edad = Label(frame, text="Edad:")
entry_edad = Entry(frame)

label_sexo = Label(frame, text="Sexo:")
entry_sexo = Entry(frame)

label_fecha_nacimiento = Label(frame, text="Fecha de nacimiento (dd/mm/aaaa):")
entry_fecha_nacimiento = Entry(frame)
entry_fecha_nacimiento.insert(0,"dd-mm-yyyy")

submit_button = Button(frame, text="Enviar", command=submit)

label_nombre.grid(row=0, column=0)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

label_apellido.grid(row=1, column=0)
entry_apellido.grid(row=1, column=1, padx=10, pady=10)

label_edad.grid(row=2, column=0)
entry_edad.grid(row=2, column=1, padx=10, pady=10)

label_sexo.grid(row=3, column=0)
entry_sexo.grid(row=3, column=1, padx=10, pady=10)

label_fecha_nacimiento.grid(row=4, column=0, padx=10, pady=10)
entry_fecha_nacimiento.grid(row=4, column=1, padx=10, pady=10)
btnNacimiento=Button(frame, text="Inserta la fecha", command=obtener_fecha_nacimiento)
btnNacimiento.grid(row=5, column=2, padx=10, pady=10)

submit_button.grid(row=5, columnspan=2)

#bucle de eventos
root.mainloop()