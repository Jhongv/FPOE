from .agregarcliente import AgregarCliente  # Importa la clase AgregarCliente del archivo agregarcliente
from .eliminarcliente import EliminarCliente  # Importa la clase EliminarCliente del archivo eliminarcliente
from .actualizarcliente import ActualizarCliente  # Importa la clase ActualizarCliente del archivo actualizarcliente
from .consultarcliente import ConsultarCliente  # Importa la clase ConsultarCliente del archivo consultarcliente
from .serviciosDeLavelopues import ServiciosLaveloPues  # Importa la clase ServiciosLaveloPues del archivo serviciosDeLavelopues
from tkinter import *

class Menu2:
    """
    Clase que representa el menú principal de la aplicación, 
    permitiendo gestionar clientes y acceder a servicios.
    """

    def agregarCliente(self):
        """
        Abre la interfaz para agregar un nuevo cliente.
        """
        agregar_cliente = AgregarCliente(self.root)  # Crea una instancia de la clase AgregarCliente
        agregar_cliente.mostrarInterfaz()  # Muestra la interfaz de agregar cliente

    def eliminarCliente(self):
        """
        Abre la interfaz para eliminar un cliente existente.
        """
        eliminar_cliente = EliminarCliente(self.root)  # Crea una instancia de la clase EliminarCliente
        eliminar_cliente.mostrarInterfaz()  # Muestra la interfaz de eliminar cliente

    def actualizarCliente(self):
        """
        Abre la interfaz para actualizar la información de un cliente existente.
        """
        actualizar_cliente = ActualizarCliente(self.root)  # Crea una instancia de la clase ActualizarCliente
        actualizar_cliente.mostrarInterfaz()  # Muestra la interfaz de actualizar cliente

    def consultarCliente(self):
        """
        Abre la interfaz para consultar la información de un cliente existente.
        """
        consultar_cliente = ConsultarCliente(self.root)  # Crea una instancia de la clase ConsultarCliente
        consultar_cliente.mostrarInterfaz()  # Muestra la interfaz de consultar cliente

    def accederAServicio1(self):
        """
        Abre la interfaz para acceder a un servicio específico.
        """
        acceder_servicio_1 = ServiciosLaveloPues(self.root)  # Crea una instancia de la clase ServiciosLaveloPues
        acceder_servicio_1.mostrarInterfaz()  # Muestra la interfaz del servicio

    def __init__(self):
        """
        Inicializa la ventana principal de la aplicación y configura el menú.
        """
        self.root = Tk()  # Crea la ventana principal

        self.root.geometry("800x600")  # Establece el tamaño de la ventana
        self.root.minsize(400, 300)  # Establece el tamaño mínimo de la ventana

        menu = Menu(self.root)  # Crea un menú para la ventana
        self.root.config(menu=menu)  # Configura el menú en la ventana

        Gestionar_clientes = Menu(menu, tearoff=0)  # Crea un submenú para gestionar clientes
        Gestionar_clientes.add_command(label='Registrar clientes', command=lambda: self.agregarCliente())
        Gestionar_clientes.add_command(label='Actualizar clientes', command=lambda: self.actualizarCliente())
        Gestionar_clientes.add_command(label='Consultar clientes', command=lambda: self.consultarCliente())
        Gestionar_clientes.add_command(label='Borrar clientes', command=lambda: self.eliminarCliente())

        Acceder_a_servicios = Menu(menu, tearoff=0)  # Crea un submenú para acceder a servicios
        Acceder_a_servicios.add_command(label='Seleccione el servicio aquí', command=lambda: self.accederAServicio1())

        menu.add_cascade(label='Gestionar clientes', menu=Gestionar_clientes)  # Añade el submenú de gestionar clientes al menú principal
        menu.add_cascade(label='Acceder a servicios', menu=Acceder_a_servicios)  # Añade el submenú de acceder a servicios al menú principal

        self.root.mainloop()  # Inicia el bucle principal de la aplicación
