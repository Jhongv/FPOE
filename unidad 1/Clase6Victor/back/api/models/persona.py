from django.db import models

class Persona(models.Model):
	nombre 				= models.TextField() #'CharField' Campo de texto
	apellido 				= models.TextField()
	estatura 		= models.IntegerField()
	peso 		= models.IntegerField()
	
	def __str__(self):
		return self.nombre