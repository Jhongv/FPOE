from django.db import models

class Servicio(models.Model):
	nombreServicio = models.TextField() #'CharField' Campo de texto
	cedula = models.TextField()
	descripcion = models.TextField()
	precio = models.IntegerField()
	
	def __str__(self):
		return self.nombreServicio