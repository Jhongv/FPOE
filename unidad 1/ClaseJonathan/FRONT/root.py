import tkinter as tk
from tkinter import *

ventana=tk.Tk()
ventana.geometry("500x500")
ventana.mainloop()

class MonedaApp:
    def _init_(self, master):
        self.master = master
        master.title("Moneda")
        master.configure(bg="#f0f0f0")
        
        # Definir las opciones de los roles
        self.roles = ["Valor", "Peso", "Tamaño", "Color", "Forma"]
        
        # Crear y colocar los elementos de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Crear el texto "Ingresar datos"
        self.lbl_ingresar = tk.Label(self.master, text="Ingresar datos", font=("Arial", 14), bg="#f0f0f0")
        self.lbl_ingresar.grid(row=0, column=0, columnspan=2, pady=10)

        # Crear y colocar etiquetas y cuadros de entrada para cada rol
        self.frames = []
        for i, rol in enumerate(self.roles):
            frame = tk.Frame(self.master, bg="#f0f0f0")
            frame.grid(row=i+1, column=0, padx=20, pady=5, sticky="ew")
            self.frames.append(frame)

            lbl_rol = tk.Label(frame, text=rol, font=("Arial", 12), bg="#f0f0f0")
            lbl_rol.pack(side=tk.LEFT)

            entry_rol = tk.Entry(frame, font=("Arial", 12), width=20)
            entry_rol.pack(side=tk.RIGHT)

        # Crear y colocar el botón "Ingresar"
        btn_ingresar = tk.Button(self.master, text="Ingresar", font=("Arial", 12, "bold"), bg="#007bff", fg="white", command=self.ingresar)
        btn_ingresar.grid(row=len(self.roles)+1, column=0, columnspan=2, pady=20, sticky="ew")

    def ingresar(self):
        # Función a ejecutar cuando se presiona el botón "Ingresar"
        print("Se presionó el botón Ingresar")


def main():
    root = tk.Tk()
    app = MonedaApp(root)
    root.mainloop()

if __name__ == "_main_":
    main()