from django.db import models

class Servicio(models.Model):
	nombreServicio = models.TextField()
	cedulaCliente = models.TextField()
	descripcion = models.TextField()
	precio = models.TextField()
	
	def __str__(self):
		return self.nombre