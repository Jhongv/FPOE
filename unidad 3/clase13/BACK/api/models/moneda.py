from django.db import models
class Moneda(models.Model):
	valor 			= models.IntegerField()
	peso			= models.TextField()
	tamaño 			= models.IntegerField()
	color			= models.TextField()
	
	def __str__(self):
		return self.valor