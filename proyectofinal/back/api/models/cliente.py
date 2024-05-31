from django.db import models

class Cliente(models.Model):
<<<<<<< HEAD
	nombre = models.TextField()
	apellido = models.TextField()
	cedula = models.TextField()
	telefono = models.TextField()
	email = models.TextField()
=======
	nombre = models.TextField() #'CharField' Campo de texto
	apellido = models.TextField()
	cedula = models.TextField()
	email = models.TextField()
	telefono= models.TextField()
>>>>>>> nr
	
	def __str__(self):
		return self.nombre