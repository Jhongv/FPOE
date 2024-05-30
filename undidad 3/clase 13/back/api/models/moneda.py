from django.db import models

class Persona(models.Model):
	valor = models.TextField() #'CharField' Campo de texto
	peso = models.TextField()
	tamaño = models.TextField()
	color = models.TextField()
	
	def __str__(self):
		return self.nombre