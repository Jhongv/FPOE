from tkinter import *

class AgregarCliente():
    def __init__(self, menuSecundario):

        self.ventana=Toplevel(menuSecundario)
        self.ventana.focus_set()
        self.ventana.title("Agregar al cliente")

    #Marco del titulo
        marcoTitulo=LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=0)


    #Se establece el contenido del marco1
        lblTitulo=Label(marcoTitulo, text="Agregar al Cliente")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)
    
    
        marco1=LabelFrame(self.ventana)
        marco1.grid(row=1, column=0)


        marco2=LabelFrame(self.ventana)
        marco2.grid(row=1, column=0)

    
    


        self.ventana.mainloop()