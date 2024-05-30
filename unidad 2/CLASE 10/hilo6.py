import threading
import time
import logging


logging.basicConfig(level = logging.DEBUG)

class Hilo6(threading.Thread):


    def __init__(self, nombre_hilo, tiempo, variable):
        threading.Thread.__init__(self, name = nombre_hilo, target = Hilo6.run)
        self.nombreHilo = nombre_hilo
        self.tiempo = tiempo
        self.variable = variable


    def setVariable(self, variable):
        self.variable = variable

    
    def run(self):
        self.guardar_nombre()



    def guardar_nombre(self):

        variable = ""
        while True:

            if self.variable == variable:
                pass

            else:
                variable = self.variable

                f = open("Name.txt", "w") 
                f.write(variable)
                f.close()
                logging.debug("Se guardó la variable"+ variable+"\n")

            time.sleep(5)


