from agregarcliente import AgregarCliente

from tkinter import *
class Menu2():

    def agregarCliente(self):
        agregar_cliente=AgregarCliente(self)

    def __init__(self):
        pass
    
        root  = Tk()

        root.geometry("800x600")
        root.minsize(400, 300)


        menu = Menu(root)
        root.config(menu = menu)


        Gestionar_clientes = Menu(menu, tearoff = 0)
        Gestionar_clientes.add_command(label = 'Registrar clientes', command=lambda:self.agregarCliente())
        Gestionar_clientes.add_command(label = 'Actualizar clientes')
        Gestionar_clientes.add_command(label = 'Consultar clientes')
        Gestionar_clientes.add_command(label = 'Borrar clientes')


        Acceder_a_servicios = Menu(menu, tearoff = 0)
        Acceder_a_servicios.add_command(label = 'Lavado + Brillado + Aspirado')
        Acceder_a_servicios.add_command(label = 'Lavado + Limpieza del motor + Porcelanizada + Aspirado')
        Acceder_a_servicios.add_command(label = 'Lavado + Brillado + Lavado de cojineria')
        Acceder_a_servicios.add_command(label = 'Lavado interno + Brillado en lámparas ')


        menu.add_cascade(label = 'Gestionar clientes', menu = Gestionar_clientes)
        menu.add_cascade(label = 'Acceder a servicios', menu = Acceder_a_servicios)







        root.mainloop()