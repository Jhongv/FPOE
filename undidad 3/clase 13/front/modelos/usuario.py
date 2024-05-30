from tkinter import *

class Usuario():
    def __init__(self, root):
        self.root=root
        self.id=StringVar(root)
        self.valor=StringVar(root)
        self.peso=StringVar(root)
        self.tamaño=StringVar(root)
        self.color=StringVar(root)
        