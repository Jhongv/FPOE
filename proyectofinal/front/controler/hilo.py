import threading
import time
import json
import os
import requests

class HiloGuardadoInfo:
    def __init__(self):
        self.url_clientes = 'http://192.168.225.145:8000/v1/cliente'
        self.url_servicios = 'http://192.168.225.145:8000/v1/servicio'
        self.file_path = os.path.join(os.getcwd(), 'informacion_clientes_servicios.txt')

    def iniciar(self):
        hilo = threading.Thread(target=self.ejecutar)
        hilo.daemon = True
        hilo.start()

    def ejecutar(self):
        while True:
            try:
                clientes = self.consultar_todo_clientes()
                servicios = self.consultar_todo_servicios()
                
                info = {
                    'clientes': clientes,
                    'servicios': servicios
                }
                
                self.guardar_info_en_archivo(info)
                time.sleep(5)  
            except Exception as e:
                print(f"Error en tarea de guardar info: {e}")

    def consultar_todo_clientes(self):
        try:
            resultado = requests.get(self.url_clientes)
            return resultado.json()
        except Exception as e:
            print(f"Error en consultar todos los clientes: {e}")
            return []

    def consultar_todo_servicios(self):
        try:
            resultado = requests.get(self.url_servicios)
            return resultado.json()
        except Exception as e:
            print(f"Error en consultar todos los servicios: {e}")
            return []

    def guardar_info_en_archivo(self, info):
        try:
            with open(self.file_path, 'w') as archivo:
                json.dump(info, archivo, indent=4)
        except Exception as e:
            print(f"Error al guardar info en archivo: {e}")
