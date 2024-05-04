from tkinter import *

class Usuario():
    def __init__(self, root):
        self.root=root
        self.nombre=StringVar(root)
        self.apellido=StringVar(root)
        self.estatura=StringVar(root)
        self.peso=StringVar(root)
        