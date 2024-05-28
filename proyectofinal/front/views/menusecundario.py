from .agregarcliente import AgregarCliente #Como todos estos archivos relacionados a la manipulación al cliente estan dentro del mismo directorio que 'menusecundario' entonces se debe colocar el punto al principio del n/archivo. en c/u
from .eliminarcliente import EliminarCliente
from .actualizarcliente import ActualizarCliente
from .consultarcliente import ConsultarCliente
from .serviciosDeLavelopues import ServiciosLaveloPues
from tkinter import *
class Menu2():

    def agregarCliente(self):
        agregar_cliente=AgregarCliente(self.root) #A todas las llamadas de la ventana por el 'self' del método agregarCliente debo colocar a la ventana 'self.root'
        agregar_cliente.mostrarInterfaz() #Sino se coloca el metodo de la clase 'AgregarCliente' denominado mostrarInterfaz, entonces solo me aparecerá la ventana con toplevel pero sin su contenido

    def eliminarCliente(self):
        eliminar_cliente=EliminarCliente(self.root)
        eliminar_cliente.mostrarInterfaz()

    def actualizarCliente(self):
        actualizar_cliente=ActualizarCliente(self.root)
        actualizar_cliente.mostrarInterfaz()

    def consultarCliente(self):
        consultar_cliente=ConsultarCliente(self.root)
        consultar_cliente.mostrarInterfaz()

    def accederAServicio1(self):
        acceder_servicio_1=ServiciosLaveloPues(self.root)
        acceder_servicio_1.mostrarInterfaz()

    def __init__(self):
        
    
        self.root  = Tk()

        self.root.geometry("800x600")
        self.root.minsize(400, 300)


        menu = Menu(self.root)
        self.root.config(menu = menu)


        Gestionar_clientes = Menu(menu, tearoff = 0)
        Gestionar_clientes.add_command(label = 'Registrar clientes', command=lambda:self.agregarCliente())
        Gestionar_clientes.add_command(label = 'Actualizar clientes', command=lambda:self.actualizarCliente())
        Gestionar_clientes.add_command(label = 'Consultar clientes', command=lambda:self.consultarCliente())
        Gestionar_clientes.add_command(label = 'Borrar clientes', command=lambda:self.eliminarCliente())


        Acceder_a_servicios = Menu(menu, tearoff = 0)
        Acceder_a_servicios.add_command(label = 'Seleccione el servicio aquí', command=lambda:self.accederAServicio1())


        menu.add_cascade(label = 'Gestionar clientes', menu = Gestionar_clientes)
        menu.add_cascade(label = 'Acceder a servicios', menu = Acceder_a_servicios)

        self.root.mainloop()