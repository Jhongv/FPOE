import threading
import time

class HiloCrearCl(threading.Thread):
    def __init__(self,nombreHilo, tiempo, variable):
        threading.Thread.__init__(self, name=nombreHilo, target=HiloCrearCl.run)
        self.nombreHilo=nombreHilo
        self.tiempo=tiempo
        self.variable=variable

    def guardarNACTC(nombre, apellido, cedula, telefono, email):
        time.sleep(2)
        with open("InfromacionCliente.txt", "a") as file:
            file.write(f"{nombre} {apellido} {cedula} {telefono} {email}\n")
