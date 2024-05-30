from django.db import models

class Cliente(models.Model):
	nombre = models.TextField()
	apellido = models.TextField()
	cedula = models.TextField()
	telefono = models.TextField()
	email = models.TextField()
	
	def __str__(self):
		return self.nombre