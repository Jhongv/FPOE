from modelo import Validador, API, Moneda
from tkinter import messagebox

class ControladorMoneda:
    def __init__(self, vista):
        self.vista = vista

    def eventoVValor(self, event):
        if Validador.validarValor(self.vista.valor.get()):
            self.vista.labelErrorValor.config(text="")
        else:
            self.vista.labelErrorValor.config(text="Valor solo debe tener números")

    def eventoVPeso(self, event):
        valorPeso = self.vista.peso.get()
        if Validador.validarPeso(valorPeso):
            self.vista.labelErrorPeso.config(text="")
        else:
            self.vista.labelErrorPeso.config(text="Peso debe tener solo números")

    def eventoVTamaño(self, event):
        valor_tamaño = self.vista.tamaño.get() 
        if Validador.validarTamaño(valor_tamaño):
            self.vista.lblErrorTamaño.config(text="")
        else:
            self.vista.lblErrorTamaño.config(text="Tamaño no cumple con lo establecido")

    def eventoVColor(self, event):
        if Validador.validarcolor(self.vista.color):
            self.vista.lblErrorcolor.config(text="")
        else:
            self.vista.lblErrorcolor.config(text="Tiene que ser un color válido")

    def validarInformacion(self):
        if (Validador.validarValor(self.vista.valor.get()) and
            Validador.validarPeso(self.vista.peso.get()) and
            Validador.validarTamaño(self.vista.tamaño.get()) and
            Validador.validarcolor(self.vista.color.get())):
        
            moneda = Moneda(self.vista.valor.get(), self.vista.peso.get(), self.vista.tamaño.get(), self.vista.color.get())
            respuesta = API.guardar_moneda(moneda)
            
            if respuesta.status_code == 200:
                messagebox.showinfo("Información", "Guardado correctamente")
            else:
                messagebox.showerror("Información", "No se pudo guardar, confirme si está correcto")
        else:
            messagebox.showerror("Información", "No se pudo guardar, confirme si está correcto")
