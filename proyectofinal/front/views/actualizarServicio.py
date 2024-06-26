from tkinter import *
import tkinter as tk
from tkinter import ttk
from controler.controlador import Validaciones
from models.modelos import Servicio
from models.modelos import Cliente
from controler.comunicador import Comunicacion
from controler.hilo import HiloGuardadoInfo
from tkinter import messagebox
from .tabla import Tabla

class ActualizarServicio:
    
    
    
    def __init__(self, menuSecundario):
        
        titulos=['Identificador','Cédula','Nombre/Servicio','Descripción','Precio']
        columnas=['id', 'cedulaCliente', 'nombreServicio', 'descripcion', 'precio']
        data=[]
        self.ventana = tk.Toplevel(menuSecundario)
        self.comunicador=Comunicacion(self.ventana)
        self.hilo_guardado_info = HiloGuardadoInfo()  
        self.hilo_guardado_info.iniciar()
        self.tabla=Tabla(self.ventana, titulos, columnas, data)
        self.cargar_tabla()

    

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
        


    
    def cargar_tabla(self):
        resultado = self.comunicador.consultar_todo_servicio('','','','')
        data = []
        for elemento in resultado:
            data.append((elemento.get('id'),elemento.get('cedula'),elemento.get('nombreServicio'),elemento.get('descripcion'),elemento.get('precio')))
        self.tabla.refrescar(data)
        
    def actualizar(self,id, cedula, nombreServicio, descripcion, precio, txtcedula, cbxnombreServicio, txtdescripcion, txtprecio):
        
        if not cedula or not nombreServicio or not descripcion or not precio:
            messagebox.showerror("ERROR", "Deben estar completos todos los campos")
        else:
            self.comunicador.actualizarServicio(id, cedula, nombreServicio, descripcion, precio)
            messagebox.showinfo("Información", "Se actualizaron los campos")
            txtcedula.delete(0, tk.END)
            cbxnombreServicio.delete(0, tk.END)
            txtdescripcion.delete(0, tk.END)
            txtprecio.delete(0, tk.END)
            self.cargar_tabla() 

            
    def mostrarInterfaz(self):
        
        def eventoVCedula(event):
            global cedula
            if Validaciones.validarCedula(servicio.cedulaCliente):
                textoVCedula = ""
            else:
                textoVCedula = "Cédula debe tener entre 7 a 10 dígitos"
            lblErrorCedula.config(text=textoVCedula)

        def eventoVerificadorExistenciaCC(event):
            cedula = txtCedulaCliente.get()
            cliente = self.comunicador.consultar(cedula)
            if cliente:
                servicio = self.comunicador.consultarServicio(cedula)
                if servicio:
                    servicio_id = servicio[0]['id']  # Suponiendo que el servicio es una lista de diccionarios y tomamos el primer elemento
                    txtId.delete(0, END)
                    txtId.insert(0, servicio_id)
                    cbxServicioEscogido.config(state='normal')
                    txtDescripcionServicio.config(state='normal')
                    txtPrecioServicio.config(state='normal')
                else:
                    messagebox.showerror("ERROR", "Servicio no encontrado para este cliente")
            else:
                messagebox.showerror("ERROR", "Cliente no encontrado")
                cbxServicioEscogido.config(state='disabled')
                txtDescripcionServicio.config(state='disabled')
                txtPrecioServicio.config(state='disabled')
        self.ventana.focus_set()
        self.ventana.title("Actualizar al servicio")
        self.ventana.resizable(0, 0)
        servicio= Servicio(self.ventana)
        

        # Marco del título
        marcoTitulo = LabelFrame(self.ventana)
        marcoTitulo.grid(row=0, column=1, padx=10, pady=10)
        lblTitulo = Label(marcoTitulo, text="Actualizar al servicio")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)
    
        marco1 = LabelFrame(self.ventana)
        marco1.grid(row=1, column=1, padx=10, pady=10)

        lblCedulaCliente=Label(marco1, text="¿Qué cliente será actualizado con un servicio?")
        lblCedulaCliente.grid(row=0, column=0)
        txtCedulaCliente=Entry(marco1, textvariable=servicio.cedulaCliente)
        txtCedulaCliente.grid(row=0, column=1)
        lblErrorCedula=Label(marco1, text="", fg="red")
        lblErrorCedula.grid(row=1, column=1)
        
        marco2=LabelFrame(self.ventana)
        marco2.grid(row=2, column=1, padx=10, pady=10)
        lblServicioEscogido=Label(marco2, text="Servicio que tiene en este momento")
        lblServicioEscogido.grid(row=0, column=0)

        cbxServicioEscogido=ttk.Combobox(marco2, values=["Lavado+Brillado+Aspirado", "Lavado+Limpieza/Motor+Porcelanizado+Aspirado", "Lavado+Brillado+Lavado/Cojinería", "Lavado Interno+Brillado/Lámparas"], textvariable=servicio.nombreServicio)
        cbxServicioEscogido.grid(row=0, column=1)

        marco3=LabelFrame(self.ventana)
        marco3.grid(row=3, column=1, padx=10, pady=10)

        lblDescripcionServicio=Label(marco3, text="Descripción")
        lblDescripcionServicio.grid(row=0, column=0)

        txtDescripcionServicio=Entry(marco3, textvariable=servicio.descripcion)
        txtDescripcionServicio.grid(row=0, column=1)

        marco4=LabelFrame(self.ventana)
        marco4.grid(row=4, column=1, padx=10, pady=10)

        lblPrecioServicio=Label(marco4, text="Precio:")
        lblPrecioServicio.grid(row=0, column=0)

        txtPrecioServicio=Entry(marco4, textvariable=servicio.precio)
        txtPrecioServicio.grid(row=0, column=1)

        marco5=LabelFrame(self.ventana)
        marco5.grid(row=5, column=1, padx=10, pady=10)

        txtId=Entry(marco5)
        txtId.grid(row=0, column=1)

        
        btnActualizarDatosCliente = Button(self.ventana, text="Actualizar", command=lambda:self.actualizar(txtId.get(), txtCedulaCliente.get(), cbxServicioEscogido.get(), txtDescripcionServicio.get(), txtPrecioServicio.get(), txtCedulaCliente, cbxServicioEscogido, txtDescripcionServicio, txtPrecioServicio))
        btnActualizarDatosCliente.grid(row=6, column=1, padx=10, pady=10)
        
        self.tabla.tabla.grid(row=9, column=0, columnspan=3)

        
        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                txtId.delete(0, END)
                txtId.insert(0, str(valores[0]))
                cbxServicioEscogido.delete(0, END)
                cbxServicioEscogido.insert(0, str(valores[2]))
                txtCedulaCliente.delete(0, END)
                txtCedulaCliente.insert(0, str(valores[1]))
                txtPrecioServicio.delete(0, END)
                txtPrecioServicio.insert(0, str(valores[4]))
                txtDescripcionServicio.delete(0, END)
                txtDescripcionServicio.insert(0, str(valores[3]))
        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        cbxServicioEscogido.bind("<<ComboboxSelected>>", lambda event: self.seleccionarServicio(event, txtCedulaCliente, cbxServicioEscogido, lblDescripcionServicio, txtPrecioServicio, lblDescripcionServicio, txtDescripcionServicio))
        txtCedulaCliente.bind("<KeyRelease>", eventoVCedula)
        txtCedulaCliente.bind("<FocusOut>", eventoVerificadorExistenciaCC)
        
        self.ventana.mainloop()
