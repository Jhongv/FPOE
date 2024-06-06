import json
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controler.controlador import Validaciones
from models.modelos import Servicio, Cliente
from controler.comunicador import Comunicacion

class ServiciosLaveloPues:
    def __init__(self, menuSecundario):
        self.ventana = tk.Toplevel(menuSecundario)
        self.comunicador = Comunicacion(self.ventana)

    def seleccionarServicio(self, event, txtCedula, cbxcomboServicio, lblprecio, txtPrecioestablecido, lblDescripcion, txtDescripcion):
        select = cbxcomboServicio.get()
        if select == "Lavado+Brillado+Aspirado":
            txtDescripcion.delete(0, tk.END)
            txtPrecioestablecido.delete(0, tk.END)
            txtDescripcion.insert(0, "Transforma tu auto:\nLavado, brillado y aspirado para un resplandor impecable\ny una frescura interior revitalizante.")
            txtPrecioestablecido.insert(0, "1000")
            lblprecio.grid(row=0, column=0)
            txtPrecioestablecido.grid(row=0, column=1)
            lblDescripcion.grid(row=0, column=0)
            txtDescripcion.grid(row=0, column=1)
        elif select == "Lavado+Limpieza/Motor+Porcelanizado+Aspirado":
            txtDescripcion.delete(0, tk.END)
            txtPrecioestablecido.delete(0, tk.END)
            txtDescripcion.insert(0, "Revitaliza tu auto:\nLavado, limpieza de motor,\nporcelanizado y aspirado para un brillo y\nrendimiento excepcionales, dentro y fuera.")
            txtPrecioestablecido.insert(0, "1200")
            lblprecio.grid(row=0, column=0)
            txtPrecioestablecido.grid(row=0, column=1)
            lblDescripcion.grid(row=0, column=0)
            txtDescripcion.grid(row=0, column=1)
        elif select == "Lavado+Brillado+Lavado/Cojinería":
            txtDescripcion.delete(0, tk.END)
            txtPrecioestablecido.delete(0, tk.END)
            txtDescripcion.insert(0, "Transforma tu auto:\nLavado exterior,\nbrillado y lavado de\ncojinería para un\nbrillo impecable y una comodidad renovada.")
            txtPrecioestablecido.insert(0, "1300")
            lblprecio.grid(row=0, column=0)
            txtPrecioestablecido.grid(row=0, column=1)
            lblDescripcion.grid(row=0, column=0)
            txtDescripcion.grid(row=0, column=1)
        elif select == "Lavado Interno+Brillado/Lámparas":
            txtDescripcion.delete(0, tk.END)
            txtPrecioestablecido.delete(0, tk.END)
            txtDescripcion.insert(0, "Renueva tu auto por dentro:\nlavado interno, brillado de\nsuperficies y\nlamparaz para un\ninterior reluciente y acogedor.")
            txtPrecioestablecido.insert(0, "4500")
            lblprecio.grid(row=0, column=0)
            txtPrecioestablecido.grid(row=0, column=1)
            lblDescripcion.grid(row=0, column=0)
            txtDescripcion.grid(row=0, column=1)

    def consultarBoton(self, cedula, labelDescripcion, textoDesc, labelPalPrecio, textoPrecio, botonAS):
        cliente = self.comunicador.consultar(cedula)
        if cliente:
            labelDescripcion.grid(row=0, column=0)
            textoDesc.grid(row=0, column=1)
            labelPalPrecio.grid(row=0, column=0)
            textoPrecio.grid(row=0, column=1)
            botonAS.config(state="normal")
            messagebox.showinfo("Información", "Cliente encontrado. Puede agregar el servicio.")
        else:
            messagebox.showerror("Información", "Cliente no encontrado. No se puede agregar el servicio.")

    def mostrarInterfaz(self):
        def eventoVCedula(event):
            global cedula
            if Validaciones.validarCedula(servicio.cedulaCliente):
                textoVCedula = ""
            else:
                textoVCedula = "Cédula debe tener entre 7 a 10 dígitos"
            lblErrorCedula.config(text=textoVCedula)

        def agregarServicio():
            cedulaV = servicio.cedulaCliente.get()
            servicioV = servicio.nombreServicio.get()
            descripcionV = servicio.descripcion.get()
            precioV = servicio.precio.get()

            if cedulaV and servicioV and descripcionV and precioV:
                resultado=self.comunicador.guardarServicio(cedulaV, servicioV, descripcionV, precioV)
                
                messagebox.showinfo("Información", "Servicio agregado correctamente.")
            else:
                messagebox.showerror("Información", "No se pudo guardar, confirme si está correcto")

        self.ventana.focus_set()
        self.ventana.title("Servicios de LaveloPues")
        self.ventana.resizable(0, 0)
        cliente = Cliente(self.ventana)
        servicio = Servicio(self.ventana)

        marcoTitulo = LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=0, padx=10, pady=10)
        lblTitulo = Label(marcoTitulo, text="Servicio 1")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        marco1 = LabelFrame(self.ventana)
        marco1.grid(row=1, column=0, padx=10, pady=10)

        lblCedulaClienteAccSer = Label(marco1, text="CC del cliente\nque va ha acceder al servicio*:")
        lblCedulaClienteAccSer.grid(row=0, column=0)
        txtCedulaClienteAccSer = Entry(marco1, textvariable=servicio.cedulaCliente)
        txtCedulaClienteAccSer.grid(row=0, column=1)
        lblErrorCedula = Label(marco1, text="", fg="red")
        lblErrorCedula.grid(row=1, column=1)
        btnConsultar = Button(marco1, text="Consultar", command=lambda: self.consultarBoton(txtCedulaClienteAccSer.get(), lblDescripcion, txtDescripcion, lblPalabraPrecio, txtPrecio, btnAgregar))
        btnConsultar.grid(row=0, column=2, padx=10, pady=10)

        marco2 = LabelFrame(self.ventana)
        marco2.grid(row=2, column=0, padx=10, pady=10)
        lblServicio = Label(marco2, text="Servicio*:")
        lblServicio.grid(row=0, column=0)
        cbxServicio = ttk.Combobox(marco2, values=["Lavado+Brillado+Aspirado", "Lavado+Limpieza/Motor+Porcelanizado+Aspirado", "Lavado+Brillado+Lavado/Cojinería", "Lavado Interno+Brillado/Lámparas"], textvariable=servicio.nombreServicio)
        cbxServicio.grid(row=0, column=1)

        marco3 = LabelFrame(self.ventana)
        marco3.grid(row=3, column=0, padx=10, pady=10)

        lblDescripcion = Label(marco3, text="Descripción:")
        lblDescripcion.grid_forget()
        txtDescripcion = ttk.Entry(marco3, justify=tk.CENTER,textvariable=servicio.descripcion)
        txtDescripcion.grid_forget()

        marco4 = LabelFrame(self.ventana)
        marco4.grid(row=4, column=0, padx=10, pady=10)

        lblPalabraPrecio = Label(marco4, text="Valor:")
        lblPalabraPrecio.grid_forget()
        txtPrecio = ttk.Entry(marco4, justify=tk.CENTER, textvariable=servicio.precio)
        txtPrecio.grid_forget()

        btnAgregar = Button(self.ventana, text="Agregar\nServicio", command=agregarServicio)
        btnAgregar.grid(row=5, column=0)
        btnAgregar.config(state="disabled")
        cbxServicio.bind("<<ComboboxSelected>>", lambda event: self.seleccionarServicio(event, txtCedulaClienteAccSer, cbxServicio, lblPalabraPrecio, txtPrecio, lblDescripcion, txtDescripcion))
        txtCedulaClienteAccSer.bind("<KeyRelease>", eventoVCedula)

        self.ventana.mainloop()

