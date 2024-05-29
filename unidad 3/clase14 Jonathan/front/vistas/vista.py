from tkinter import *
from controlador.controlador import ControladorMoneda
from modelos.usuario import Usuario
import re
from tkinter import messagebox
import requests
from controlador.comunicacion import Comunicacion
from .tabla import Tabla


class Interfaz():


    def __init__(self):
        titulos=["Identificador", "Valor", "Peso", "Tamaño", "Color"]
        columnas=["id", "valor","Peso", "tamaño", "color"]
        data=[]
        self.root=Tk()
        self.comunicador=Comunicacion(self.root)
        self.tabla=Tabla(self.root, titulos, columnas, data)
        pass

    def accion_guardar_boton(self, id, valor, peso, tamaño, color):
        if id =='':
            self.comunicador.guardar(valor, peso, tamaño, color)
        else:
            self.comunicador.actualizar(id, valor, peso, tamaño, color)
        self.tabla.refrescar()

    def accion_consultar_boton(self, lblConsultarvalor,lblConsultarId, id):
        resultado = self.comunicador.consultar(id)
        print(resultado)
        print(type(resultado))
        lblConsultarvalor.config(text = resultado.get('valor'))
        lblConsultarId.config(text = resultado.get('color'))
    
    def accion_consultar_todo(self, valor, peso, tamaño, color):
        resultado = self.comunicador.consultar_todo(valor, peso, tamaño, color)
        data=[]
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('valor'), elemento.get('peso'), elemento.get('tamaño'), elemento.get('color')))
        self.tabla.refrescar(data)
        
        #print(resultado[0].get('color'))
        #print(type(resultado))


        
    def mostrar_interfaz(self):
        
    
        def eventoVvalor(event):
            global valor
            if ControladorMoneda.validarvalor(usuario.valor): # type: ignore
                textoVvalor=""
            else:
                textoVvalor="valor debe tener solo letras"
            labelErrorvalor.config(text=textoVvalor)
 
        def eventoVpeso(event):
            global peso
            if ControladorMoneda.validarpeso(usuario.peso): # type: ignore
                textoVpeso=""
            else:
                textoVpeso="peso debe tener solo letras"
            labelErrorpeso.config(text=textoVpeso)

        def eventoVtamaño(event):
            global tamaño
            if ControladorMoneda.validartamaño(usuario.tamaño): # type: ignore
                textoVtamaño=""
            else:
                textoVtamaño="tamaño no cumple con lo establecido"
            lblErrortamaño.config(text=textoVtamaño)

        def eventoVcolor(event):
            global color
            if ControladorMoneda.validarcolor(usuario.color): # type: ignore
                textoVcolor=""
            else:
                textoVcolor="color no cumple con lo establecido"
            lblErrorcolor.config(text=textoVcolor)


        def validarInformacion():
            ValoreventoVValorV = re.match(r"^[A-Za-zñÑ ]*$", usuario.valor.get())
            PesoV = re.match(r"^[A-Za-zñÑ ]*$", usuario.peso.get())
            TamañoeventoVTamañoV = re.match(r"^\d{1}(\.\d{0,2})?$", usuario.tamaño.get())
            ColoreventoVColorV = re.match(r"^\d{1,3}(\.\d{0,2})?$", usuario.color.get())


            if ValoreventoVValorV and PesoV and TamañoeventoVTamañoV and ColoreventoVColorV:
        
                data = {
                    "ValoreventoVValor": usuario.valor.get(),
                    "Peso": usuario.peso.get(),
                    "TamañoeventoVTamaño": usuario.tamaño.get(),
                    "ColoreventoVColor": usuario.color.get()
            }
                respuesta = requests.post("http://127.0.0.1:8000/v1/moneda", data)
                print(respuesta.status_code)
                print(respuesta.content)
        
                messagebox.showinfo("Informacion", "Se guardo correctamente")
            else:
                messagebox.showerror("Informacion", "No se pudo guardar, confirme si está correcto")


        self.root.title("Clase Moneda")
        #self.root.resizable(0,0)
        usuario=Usuario(self.root)

        marcotitulo=LabelFrame(self.root)
        marcotitulo.grid(row=0, column=1, padx=5, pady=5)

        lblTitulo=Label(marcotitulo, text="Clase-Moneda")
        lblTitulo.grid(row=0, column=0, padx=10, pady=10)

        marcoAtr1=LabelFrame(self.root)
        marcoAtr1.grid(row=1, column=0, padx=5, pady=5)

        lblAtr1=Label(marcoAtr1, text="Ingrese el valor*\nTenga en cuenta que solo son números, sin caracteres especiales o letras:")
        lblAtr1.grid(row=0, column=0)
        txtAtr1=Entry(marcoAtr1, textvariable=usuario.valor)
        txtAtr1.grid(row=0,column=1, padx=10, pady=10)
        labelErrorvalor=Label(marcoAtr1, text="", fg="red")
        labelErrorvalor.grid(row=1, column=1)

        marcoAtr2=LabelFrame(self.root)
        marcoAtr2.grid(row=2, column=0, padx=5, pady=5)

        lblAtr2=Label(marcoAtr2, text="Ingrese el peso*\nTenga en cuenta que solo son números, sin caracteres especiales o letras:")
        lblAtr2.grid(row=0,column=0)
        txtAtr2=Entry(marcoAtr2, textvariable=usuario.peso)
        txtAtr2.grid(row=0, column=1, padx=10, pady=10)
        labelErrorpeso=Label(marcoAtr2, text="", fg="red")
        labelErrorpeso.grid(row=1, column=1)

        marcoAtr3=LabelFrame(self.root)
        marcoAtr3.grid(row=1, column=2, padx=5, pady=5)

        lblAtr3=Label(marcoAtr3, text="Ingrese el tamaño:")
        lblAtr3.grid(row=0,column=0)
        txtAtr3=Entry(marcoAtr3, textvariable=usuario.tamaño)
        txtAtr3.grid(row=0, column=1, padx=10, pady=10)
        lblErrortamaño=Label(marcoAtr3, text="", fg="red")
        lblErrortamaño.grid(row=1, column=1)

        marcoAtr4=LabelFrame(self.root)
        marcoAtr4.grid(row=2,column=2, padx=5, pady=5)

        lblAtr4=Label(marcoAtr4, text="Ingrese el color:")
        lblAtr4.grid(row=0,column=0)
        txtAtr4=Entry(marcoAtr4, textvariable=usuario.color)
        txtAtr4.grid(row=0, column=1, padx=10, pady=10)
        lblErrorcolor=Label(marcoAtr4, text="", fg="red")
        lblErrorcolor.grid(row=1, column=1)
        btnGuardar=Button(self.root, text="Guardar", padx=10, pady=10, command=validarInformacion)
        btnGuardar.grid(row=3, column=1, padx=10, pady=10)

        marco5=LabelFrame(self.root)
        marco5.grid(row=3,column=2, padx=5, pady=5)


        lblConsultarvalor=Label(marco5, text="")
        lblConsultarvalor.grid(row=0, column=0)
        lblConsultarId=Label(marco5, text="")
        lblConsultarId.grid(row=0,column=1)
        btnGuardar2=Button(marco5,text="Guardar 2", command=lambda: self.accion_guardar_boton(txtId.get(), txtAtr1.get(),txtAtr2.get(), txtAtr3.get(), txtAtr4.get()))
        btnGuardar2.grid(row=1,column=0, padx=10, pady=10)
        btnConsultar1=Button(marco5, text="Consultar 1", command=lambda:self.accion_consultar_boton(lblConsultarvalor, lblConsultarId,txtAtr4.get()))
        btnConsultar1.grid(row=1, column=1, padx=10, pady=10)
        btnConsultarTodo=Button(marco5, text="Consultar todo", command=lambda:self.accion_consultar_todo(txtAtr1.get(), txtAtr2.get(), txtAtr3.get(), txtAtr4.get()))
        btnConsultarTodo.grid(row=1, column=2, padx=10, pady=10)

        marco6=LabelFrame(self.root)
        marco6.grid(row=4,column=2, padx=5, pady=5)

        lblId=Label(marco6)
        lblId.grid(row=0, column=0)
        txtId=Entry(marco6)
        txtId.grid(row=0, column=1)
        self.tabla.tabla.grid(row=5,column=0, columnspan=3)

        def seleccionar_elemento(_):
                for i in self.tabla.tabla.selection():
                    valores=self.tabla.tabla.item(i)['values']
                    txtId.delete(0, END)
                    txtId.insert(0, str(valores[0]))
                    txtAtr1.delete(0, END)
                    txtAtr1.insert(0, str(valores[1]))
                    txtAtr2.delete(0, END)
                    txtAtr2.insert(0, str(valores[2]))
                    txtAtr3.delete(0, END)
                    txtAtr3.insert(0, str(valores[3]))
                    txtAtr4.delete(0, END)
                    txtAtr4.insert(0, str(valores[4]))

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicador.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)


        self.tabla.tabla.bind("<<TreeviewSelect>>", seleccionar_elemento)
        self.tabla.tabla.bind("<Delete>", borrar_elemento)
        txtAtr1.bind("<KeyRelease>", eventoVvalor)
        txtAtr2.bind("<KeyRelease>", eventoVpeso)
        txtAtr3.bind("<KeyRelease>", eventoVtamaño)
        txtAtr4.bind("<KeyRelease>", eventoVcolor)
        self.root.mainloop()
