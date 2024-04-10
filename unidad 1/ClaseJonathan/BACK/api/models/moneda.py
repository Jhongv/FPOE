from django.db import models
class Moneda(models.Model):
	valor 			= models.CharField(max_length=50, null=False, blank=True)
	peso			= models.TextField(max_length=5000, null=False, blank=True)
	tamaño 			= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	color			= models.DateTimeField(auto_now=True, verbose_name="date updated")
	
	def __str__(self):
		return self.valor