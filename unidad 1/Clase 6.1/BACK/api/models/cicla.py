from django.db import models
class Cicla(models.Model):
	marca 			= models.CharField(max_length=50, null=False, blank=True)
	talla			= models.TextField(max_length=5000, null=False, blank=True)
	componentes 	= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	valor			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	
	def __str__(self):
		return self.valor