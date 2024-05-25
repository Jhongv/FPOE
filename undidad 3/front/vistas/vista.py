from tkinter import *
from controladores.controlador import Validaciones
from modelos.usuario import Usuario
import re
from tkinter import messagebox
import requests
from controladores.comunicacion import Comunicacion
from .tabla import Tabla
class Interfaz():

    def __init__(self):
        titulos=['Identificador','Nombre','Apellido','Estatura','Peso']
        columnas=['id', 'nombre', 'apellido', 'estatura', 'peso']
        data=[]
        self.root=Tk()
        self.comunicador=Comunicacion(self.root)
        self.tabla=Tabla(self.root, titulos, columnas, data)
        pass

    def accion_guardar_boton(self, id, nombre, apellido, estatura, peso):
        if id == '':
            self.comunicador.guardar(nombre, apellido, estatura, peso)
        else:
            self.comunicador.actualizar(id, nombre, apellido, estatura, peso)

    def accion_consultar_boton(self, lblConsultarNombre,lblConsultarPeso, id):
        
        resultado=self.comunicador.consultar(id)
        print(resultado)
        print(type(resultado))
        lblConsultarNombre.config(text=resultado.get('nombre'))
        lblConsultarPeso.config(text=resultado.get('peso'))
        
    
    def accion_consultar_todo(self, nombre, apellido, estatura, peso):
        resultado=self.comunicador.consultar_todo(nombre, apellido, estatura, peso)
        data=[]
        for elemento in resultado:
            data.append((elemento.get('id'),elemento.get('nombre'),elemento.get('apellido'),elemento.get('estatura'),elemento.get('peso')))
        self.tabla.refrescar(data)


        
    def mostrar_interfaz(self):
        
    
        def eventoVnombre(event):
            global nombre
            if Validaciones.validarNombre(usuario.nombre):
                textoVnombre=""
            else:
                textoVnombre="Nombre debe tener solo letras"
            labelErrorNombre.config(text=textoVnombre)

        def eventoVApellido(event):
            global apellido
            if Validaciones.validarApellido(usuario.apellido):
                textoVapellido=""
            else:
                textoVapellido="Apellido debe tener solo letras"
            labelErrorApellido.config(text=textoVapellido)

        def eventoVEstatura(event):
            global estatura
            valor_estatura = txtAtr3.get() 
            if Validaciones.validarEstatura(usuario.estatura):
                textoVEstatura=""
            else:
                textoVEstatura="Estatura no cumple con lo establesido"
            lblErrorEstatura.config(text=textoVEstatura)

        def eventoVPeso(event):
            global peso
            valorPeso = txtAtr4.get() 
            if Validaciones.validarPeso(usuario.peso):
                textoVpeso=""
            else:
                textoVpeso="Peso no cumple con lo establesido"
            lblErrorPeso.config(text=textoVpeso)

        def validarInformacion():
        
            nombreV = re.match(r"^[A-Za-zñÑ ]*$", usuario.nombre.get())
            apellidoV = re.match(r"^[A-Za-zñÑ ]*$", usuario.apellido.get())
            estaturaV = re.match(r"^\d{1}(\.\d{0,2})?$", usuario.estatura.get())
            pesoV = re.match(r"^\d{1,3}(\.\d{0,2})?$", usuario.peso.get())


            if nombreV and apellidoV and estaturaV and pesoV:
                
                data = {
                    "nombre": usuario.nombre.get(),
                    "apellido": usuario.apellido.get(),
                    "estatura": usuario.estatura.get(),
                    "peso": usuario.peso.get()
                }
                respuesta = requests.post("http://127.0.0.1:8000/v1/persona", data)
                print(respuesta.status_code)
                print(respuesta.content)
                
                messagebox.showinfo("Informacion", "Se guardo correctamente")
            else:
                messagebox.showerror("Informacion", "No se pudo guardar, confirme si está correcto")
        
        self.root.title("Clase persona")
        #self.root.resizable(0,0)
        usuario=Usuario(self.root)

        marcotitulo=LabelFrame(self.root)
        marcotitulo.grid(row=0, column=1, padx=5, pady=5)

        lblTitulo=Label(marcotitulo, text="Clase-Persona")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        marcoAtr1=LabelFrame(self.root)
        marcoAtr1.grid(row=1, column=0, padx=5, pady=5)

        lblAtr1=Label(marcoAtr1, text="Ingrese el 1er atributo de Cl/Persona(Nombre)*\nTenga en cuenta que solo son letras, sin caracteres especiales o números:")
        lblAtr1.grid(row=0, column=0)
        txtAtr1=Entry(marcoAtr1, textvariable=usuario.nombre)
        txtAtr1.grid(row=0,column=1, padx=10, pady=10)
        labelErrorNombre=Label(marcoAtr1, text="", fg="red")
        labelErrorNombre.grid(row=1, column=1)

        marcoAtr2=LabelFrame(self.root)
        marcoAtr2.grid(row=2, column=0, padx=5, pady=5)

        lblAtr2=Label(marcoAtr2, text="Ingrese el 2do atributo de Cl/Persona(Apellido)*\nTenga en cuenta que solo son letras, sin caracteres especiales o números:")
        lblAtr2.grid(row=0,column=0)
        txtAtr2=Entry(marcoAtr2, textvariable=usuario.apellido)
        txtAtr2.grid(row=0, column=1, padx=10, pady=10)
        labelErrorApellido=Label(marcoAtr2, text="", fg="red")
        labelErrorApellido.grid(row=1, column=1)

        marcoAtr3=LabelFrame(self.root)
        marcoAtr3.grid(row=1, column=2, padx=5, pady=5)

        lblAtr3=Label(marcoAtr3, text="Ingrese el 3er atributo de Cl/Persona(Estatura(metros)/Decimal)\nTenga en cuenta esta forma de inserción\nd--> dígito; 1d unico antes del punto y max 2d después de este:")
        lblAtr3.grid(row=0,column=0)
        txtAtr3=Entry(marcoAtr3, textvariable=usuario.estatura)
        txtAtr3.grid(row=0, column=1, padx=10, pady=10)
        lblErrorEstatura=Label(marcoAtr3, text="", fg="red")
        lblErrorEstatura.grid(row=1, column=1)

        marcoAtr4=LabelFrame(self.root)
        marcoAtr4.grid(row=2,column=2, padx=5, pady=5)

        lblAtr4=Label(marcoAtr4, text="Ingrese el 4to atributo de Cl/Persona(Peso(Kg)/Decimal)*\nTenga en cuenta esta forma de inserción\nd--> dígito max 3d antes del . y max 2d después de este:")
        lblAtr4.grid(row=0,column=0)
        txtAtr4=Entry(marcoAtr4, textvariable=usuario.peso)
        txtAtr4.grid(row=0, column=1, padx=10, pady=10)
        lblErrorPeso=Label(marcoAtr4, text="", fg="red")
        lblErrorPeso.grid(row=1, column=1)
        btnGuardar=Button(self.root, text="Guardar", padx=10, pady=10, command=validarInformacion)
        btnGuardar.grid(row=3, column=1, padx=10, pady=10)

        marco5=LabelFrame(self.root)
        marco5.grid(row=3,column=2, padx=5, pady=5)

        lblConsultarNombre=Label(marco5, text="")
        lblConsultarNombre.grid(row=0, column=0)
        lblConsultarPeso=Label(marco5, text="")
        lblConsultarPeso.grid(row=0,column=1)
        btnGuardar2=Button(marco5,text="Guardar 2", command=lambda: self.accion_guardar_boton(txtId.get(), txtAtr1.get(), txtAtr2.get(), txtAtr3.get(), txtAtr4.get()))
        btnGuardar2.grid(row=1,column=0, padx=10, pady=10)
        btnConsultar1=Button(marco5, text="Consultar 1", command=lambda:self.accion_consultar_boton(lblConsultarNombre,lblConsultarPeso, txtAtr4.get()))
        btnConsultar1.grid(row=1, column=1, padx=10, pady=10)
        btnConsultarTodo=Button(marco5, text="Consultar todo", command=lambda:self.accion_consultar_todo(txtAtr1.get(), txtAtr2.get(), txtAtr3.get(), txtAtr4.get()))
        btnConsultarTodo.grid(row=1, column=2, padx=10, pady=10)
        
        marco6=LabelFrame(self.root)
        marco6.grid(row=4,column=2, padx=5, pady=5)

        lblId=Label(marco6, text="Id", textvariable=usuario.id)
        lblId.grid(row=0, column=0)
        txtId=Entry(marco6)
        txtId.grid(row=0, column=1)
        
        self.tabla.tabla.grid(row=5, column=0, columnspan=3)

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                txtId.delete(0, END)
                txtId.insert(0, str(valores[0]))
                txtAtr1.delete(0, END)
                txtAtr1.insert(0, str(valores[1]))
                txtAtr2.delete(0, END)
                txtAtr2.insert(0, str(valores[2]))
                txtAtr3.delete(0, END)
                txtAtr3.insert(0, str(valores[3]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicador.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        txtAtr1.bind("<KeyRelease>", eventoVnombre)
        txtAtr2.bind("<KeyRelease>", eventoVApellido)
        txtAtr3.bind("<KeyRelease>", eventoVEstatura)
        txtAtr4.bind("<KeyRelease>", eventoVPeso)
        self.root.mainloop()
