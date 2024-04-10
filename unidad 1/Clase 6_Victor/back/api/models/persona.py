from django.db import models

class Post(models.Model):
	nombre 				= models.TextField(max_length=50, null=False, blank=True) #'CharField' Campo de texto
	apellido 				= models.TextField(max_length=5000, null=False, blank=True)
	estatura 		= models.IntegerField(auto_now_add=True, verbose_name="date published")
	peso 		= models.IntegerField(auto_now=True, verbose_name="date updated")
	
	def __str__(self):
		return self.nombre
# Create your models here.