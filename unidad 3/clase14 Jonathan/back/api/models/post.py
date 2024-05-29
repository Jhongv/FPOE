from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel
class Post(TimeStampedModel, SoftDeletableModel):
	title 				= models.CharField(max_length=50, null=False, blank=True) #'CharField' Campo de texto
	body 				= models.TextField(max_length=5000, null=False, blank=True)
	date_published 		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated") #verbose_name Se usa pa los comentarios
	slug 				= models.SlugField(blank=True, unique=True)
	def __str__(self):
		return self.title
