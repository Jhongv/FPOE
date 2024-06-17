from tkinter import *

class Cliente():
    def __init__(self, root):
        self.root=root
        self.id=StringVar()
        self.nombre=StringVar()
        self.apellido=StringVar()
        self.cedula=StringVar()
        self.email=StringVar()
        self.telefono=StringVar()
        
class Servicio():
    def __init__(self, root):
        self.root=root
        self.id=StringVar()
        self.nombreServicio=StringVar()
        self.cedulaCliente=StringVar()
        self.descripcion=StringVar()
        self.precio=IntVar()

    
        