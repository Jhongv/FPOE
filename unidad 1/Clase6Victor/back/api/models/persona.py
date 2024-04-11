from django.db import models

class Persona(models.Model):
	nombre 				= models.TextField() #'CharField' Campo de texto
	apellido 				= models.TextField()
	estatura 		= models.DecimalField(max_digits=4, decimal_places=2)
	peso 		= models.DecimalField(max_digits=4, decimal_places=2)
	
	def __str__(self):
		return self.nombre