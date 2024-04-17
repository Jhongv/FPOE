from django.db import models

class Persona(models.Model):
	nombre = models.TextField() #'CharField' Campo de texto
	apellido = models.TextField()
	estatura = models.TextField()
	peso = models.TextField()
	
	def __str__(self):
		return self.nombre