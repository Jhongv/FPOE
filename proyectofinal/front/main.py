from tkinter import *

root = Tk()

root.geometry("800x600")
root.minsize(400, 300)


menu = Menu(root)
root.config(menu = menu)


Gestionar_clientes = Menu(menu, tearoff = 0)
Gestionar_clientes.add_command(label = 'Registrar clientes')
Gestionar_clientes.add_command(label = 'Actualizar clientes')
Gestionar_clientes.add_command(label = 'Consultar clientes')
Gestionar_clientes.add_command(label = 'Borrar clientes')


Acceder_a_servicios = Menu(menu, tearoff = 0)
Acceder_a_servicios.add_command(label = 'Lavar carro')
Acceder_a_servicios.add_command(label = 'Lavar moto')


menu.add_cascade(label = 'Gestionar clientes', menu = Gestionar_clientes)
menu.add_cascade(label = 'Acceder a servicios', menu = Acceder_a_servicios)







root.mainloop()