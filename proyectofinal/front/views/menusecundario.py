from .agregarcliente import AgregarCliente  # Importa la clase AgregarCliente del archivo agregarcliente
from .eliminarcliente import EliminarCliente  # Importa la clase EliminarCliente del archivo eliminarcliente
from .actualizarcliente import ActualizarCliente  # Importa la clase ActualizarCliente del archivo actualizarcliente
from .consultarcliente import ConsultarCliente  # Importa la clase ConsultarCliente del archivo consultarcliente
from .agregarServicio import AgregarServicio  # Importa la clase ServiciosLaveloPues del archivo serviciosDeLavelopues
from .consultarServicios import ConsultarServicios
from .actualizarServicio import ActualizarServicio
from .eliminarServicio import EliminarServicio

from tkinter import *

class Menu2:
    

    def agregarCliente(self):
        
        agregar_cliente = AgregarCliente(self.root)  # Crea una instancia de la clase AgregarCliente
        agregar_cliente.mostrarInterfaz()  # Muestra la interfaz de agregar cliente

    def eliminarCliente(self):
        
        eliminar_cliente = EliminarCliente(self.root)  # Crea una instancia de la clase EliminarCliente
        eliminar_cliente.mostrarInterfaz()  # Muestra la interfaz de eliminar cliente

    def actualizarCliente(self):
        
        actualizar_cliente = ActualizarCliente(self.root)  # Crea una instancia de la clase ActualizarCliente
        actualizar_cliente.mostrarInterfaz()  # Muestra la interfaz de actualizar cliente

    def consultarCliente(self):
        
        consultar_cliente = ConsultarCliente(self.root)  # Crea una instancia de la clase ConsultarCliente
        consultar_cliente.mostrarInterfaz()  # Muestra la interfaz de consultar cliente

    def accederAServicio1(self):
        
        acceder_servicio_1 = AgregarServicio(self.root)  # Crea una instancia de la clase ServiciosLaveloPues
        acceder_servicio_1.mostrarInterfaz()  # Muestra la interfaz del servicio

    def consultarServicio(self):
        consultar_servicio=ConsultarServicios(self.root)
        consultar_servicio.mostrarInterfaz()

    def actualizarServicio(self):
        actualizar_servicio=ActualizarServicio(self.root)
        actualizar_servicio.mostrarInterfaz()

    def eliminarServicio(self):
        eliminar_servicio=EliminarServicio(self.root)
        eliminar_servicio.mostrarInterfaz()

    def __init__(self):
        
        self.root = Tk()  

        self.root.geometry("400x200")  
        self.root.resizable(0,0) 
        self.root.title("LaveloPues S.A.S") 

        menu = Menu(self.root)  
        self.root.config(menu=menu)  

        Gestionar_clientes = Menu(menu, tearoff=0)  
        Gestionar_clientes.add_command(label='Registrar clientes', command=lambda: self.agregarCliente())
        Gestionar_clientes.add_command(label='Actualizar clientes', command=lambda: self.actualizarCliente())
        Gestionar_clientes.add_command(label='Consultar clientes', command=lambda: self.consultarCliente())
        Gestionar_clientes.add_command(label='Borrar clientes', command=lambda: self.eliminarCliente())

        Acceder_a_servicios = Menu(menu, tearoff=0)  
        Acceder_a_servicios.add_command(label='Seleccione el servicio aquí', command=lambda: self.accederAServicio1())
        Acceder_a_servicios.add_command(label='Consulta los servicios', command=lambda: self.consultarServicio())
        Acceder_a_servicios.add_command(label="Actualizar Servicios", command=lambda:self.actualizarServicio())
        Acceder_a_servicios.add_command(label="Eliminar Servicios", command=lambda:self.eliminarServicio())

        menu.add_cascade(label='Gestionar clientes', menu=Gestionar_clientes)  
        menu.add_cascade(label='Acceder a servicios', menu=Acceder_a_servicios)  

        self.root.mainloop()  
