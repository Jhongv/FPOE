from django.db import models

class Cliente(models.Model):
	nombre = models.TextField() #'CharField' Campo de texto
	apellido = models.TextField()
	cedula = models.TextField()
	email = models.TextField()
	telefono = models.TextField()
	
	def __str__(self):
		return self.nombre