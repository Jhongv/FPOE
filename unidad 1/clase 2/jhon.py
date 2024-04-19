import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def submit():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    sexo = entry_sexo.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()


    mensaje = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nSexo: {sexo}\nFecha de nacimiento: {fecha_nacimiento}"
    messagebox.showinfo("Información ingresada", mensaje)

root = tk.Tk()
root.title("Formulario")

label_nombre = tk.Label(root, text="Nombre:")
entry_nombre = tk.Entry(root)

label_apellido = tk.Label(root, text="Apellido:")
entry_apellido = tk.Entry(root)

label_edad = tk.Label(root, text="Edad:")
entry_edad = tk.Entry(root)

label_sexo = tk.Label(root, text="Sexo:")
entry_sexo = tk.Entry(root)

label_fecha_nacimiento = tk.Label(root, text="Fecha de nacimiento (dd/mm/aaaa):")
entry_fecha_nacimiento = tk.Entry(root)

submit_button = tk.Button(root, text="Enviar", command=submit)

label_nombre.grid(row=0, column=0)
entry_nombre.grid(row=0, column=1)

label_apellido.grid(row=1, column=0)
entry_apellido.grid(row=1, column=1)

label_edad.grid(row=2, column=0)
entry_edad.grid(row=2, column=1)

label_sexo.grid(row=3, column=0)
entry_sexo.grid(row=3, column=1)

label_fecha_nacimiento.grid(row=4, column=0)
entry_fecha_nacimiento.grid(row=4, column=1)

submit_button.grid(row=5, columnspan=2)

#bucle de eventos
root.mainloop()