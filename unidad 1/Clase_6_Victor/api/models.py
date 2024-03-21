from django.db import models
from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
class Post():
	title 				= models.CharField(max_length=50, null=False, blank=True) #'CharField' Campo de texto
	nombre 				= models.TextField(max_length=5000, null=False, blank=True)
	apellido 		= models.TextField(auto_now_add=True, verbose_name="date published")
	peso 		= models.FloatField(auto_now=True, verbose_name="date updated") #verbose_name Se usa pa los comentarios
	estatura 				= models.IntegerField(blank=True, unique=True)
	def __str__(self):
		return self.title
# Create your models here.
