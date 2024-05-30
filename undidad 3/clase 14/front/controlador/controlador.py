from modelos import usuario
from tkinter import messagebox

class ControladorMoneda:
    def __init__(self, vista):
        self.vista = vista

    def eventoVValor(self, event):
        if usuario.validarValor(self.vista.valor.get()):
            self.vista.labelErrorValor.config(text="")
        else:
            self.vista.labelErrorValor.config(text="Valor solo debe tener números")

    def eventoVPeso(self, event):
        valorPeso = self.vista.peso.get()
        if usuario.validarPeso(valorPeso):
            self.vista.labelErrorPeso.config(text="")
        else:
            self.vista.labelErrorPeso.config(text="Peso debe tener solo números")

    def eventoVTamaño(self, event):
        valor_tamaño = self.vista.tamaño.get() 
        if usuario.validarTamaño(valor_tamaño):
            self.vista.lblErrorTamaño.config(text="")
        else:
            self.vista.lblErrorTamaño.config(text="Tamaño no cumple con lo establecido")

    def eventoVColor(self, event):
        if usuario.validarcolor(self.vista.color):
            self.vista.lblErrorcolor.config(text="")
        else:
            self.vista.lblErrorcolor.config(text="Tiene que ser un color válido")

    def validarInformacion(self):
        if (usuario.validarValor(self.vista.valor.get()) and
            usuario.validarPeso(self.vista.peso.get()) and
            usuario.validarTamaño(self.vista.tamaño.get()) and
            usuario.validarcolor(self.vista.color.get())):
        
            moneda = moneda(self.vista.valor.get(), self.vista.peso.get(), self.vista.tamaño.get(), self.vista.color.get())
            respuesta = API.guardar_moneda(moneda) # type: ignore
            
            if respuesta.status_code == 200:
                messagebox.showinfo("Información", "Guardado correctamente")
            else:
                messagebox.showerror("Información", "No se pudo guardar, confirme si está correcto")
        else:
            messagebox.showerror("Información", "No se pudo guardar, confirme si está correcto")
    

    