from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Clase persona")
root.resizable(0,0)

marcotitulo=LabelFrame(root)
marcotitulo.grid(row=0, column=1, padx=5, pady=5)

lblTitulo=Label(marcotitulo, text="Clase-Persona")
lblTitulo.grid(row=0, column=0, padx=10, pady=10)

marcoAtr1=LabelFrame(root)
marcoAtr1.grid(row=1, column=0, padx=5, pady=5)

lblAtr1=Label(marcoAtr1, text="Ingrese el 1er atributo de Cl/Persona*:")
lblAtr1.grid(row=0, column=0)
txtAtr1=Entry(marcoAtr1)
txtAtr1.grid(row=0,column=1, padx=10, pady=10)

marcoAtr2=LabelFrame(root)
marcoAtr2.grid(row=2, column=0, padx=5, pady=5)

lblAtr2=Label(marcoAtr2, text="Ingrese el 2do atributo de Cl/Persona*:")
lblAtr2.grid(row=0,column=0)
txtAtr2=Entry(marcoAtr2)
txtAtr2.grid(row=0, column=1, padx=10, pady=10)


marcoAtr3=LabelFrame(root)
marcoAtr3.grid(row=1, column=2, padx=5, pady=5)

lblAtr3=Label(marcoAtr3, text="Ingrese el 3er atributo de Cl/Persona*:")
lblAtr3.grid(row=0,column=0)
txtAtr3=Entry(marcoAtr3)
txtAtr3.grid(row=0, column=1, padx=10, pady=10)

marcoAtr4=LabelFrame(root)
marcoAtr4.grid(row=2,column=2, padx=5, pady=5)

lblAtr4=Label(marcoAtr4, text="Ingrese el 4to atributo de Cl/Persona*:")
lblAtr4.grid(row=0,column=0)
txtAtr4=Entry(marcoAtr4)
txtAtr4.grid(row=0, column=1, padx=10, pady=10)

btnGuardar=Button(root, text="Guardar", padx=10, pady=10)
btnGuardar.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()