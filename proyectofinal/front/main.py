import tkinter as tk
from tkinter import StringVar, messagebox


class LavelopuesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lavelopues App")

        # Cliente variables
        self.client_name = tk.StringVar()
        self.client_email = tk.StringVar()
        self.client_phone = tk.StringVar()
        self.client_address = tk.StringVar()

        # Servicio variables
        self.service_name = tk.StringVar()
        self.service_description = tk.StringVar()

        # Cliente frame
        client_frame = tk.Frame(self.master)
        client_frame.pack(padx=10, pady=10)

        tk.Label(client_frame, text="Nombre del Cliente:").grid(row=0, column=0)
        tk.Entry(client_frame, textvariable=self.client_name).grid(row=0, column=1)
        tk.Label(client_frame, text="Email del Cliente:").grid(row=1, column=0)
        tk.Entry(client_frame, textvariable=self.client_email).grid(row=1, column=1)
        tk.Label(client_frame, text="Teléfono del Cliente:").grid(row=2, column=0)
        tk.Entry(client_frame, textvariable=self.client_phone).grid(row=2, column=1)
        tk.Label(client_frame, text="Dirección del Cliente:").grid(row=3, column=0)
        tk.Entry(client_frame, textvariable=self.client_address).grid(row=3, column=1)

        tk.Button(client_frame, text="Registrar Cliente", command=self.register_client).grid(row=4, columnspan=2, pady=5)

        # Servicio frame
        service_frame = tk.Frame(self.master)
        service_frame.pack(padx=10, pady=10)

        tk.Label(service_frame, text="Nombre del Servicio:").grid(row=0, column=0)
        #tk.Entry(service_frame, textvariable=self.service_name).grid(row=0, column=1)

        servicios = StringVar()
        servicios.set('Elija un servicio')

        menu_services = tk.OptionMenu(service_frame, servicios, 'Lavar auto', 'Lavar moto').grid(row = 0, column = 1)
        
        tk.Label(service_frame, text="Descripción del Servicio:").grid(row=1, column=0)
        tk.Entry(service_frame, textvariable=self.service_description).grid(row=1, column=1)

        tk.Button(service_frame, text="Registrar Servicio", command=self.register_service).grid(row=2, columnspan=2, pady=5)

    def register_client(self):
        client_name = self.client_name.get()
        client_email = self.client_email.get()
        client_phone = self.client_phone.get()
        client_address = self.client_address.get()
        # Aquí iría la lógica para registrar el cliente en la base de datos de lavelopues

        messagebox.showinfo("Cliente Registrado", f"Cliente {client_name} registrado correctamente.")

    def register_service(self):
        service_name = self.service_name.get()
        service_description = self.service_description.get()
        # Aquí iría la lógica para registrar el servicio en la base de datos de lavelopues

        messagebox.showinfo("Servicio Registrado", f"Servicio {service_name} registrado correctamente.")


def main():
    root = tk.Tk()
    app = LavelopuesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()