from django.contrib import admin
from .models.post import Post
admin.site.register(Post)
from .models.cliente import Cliente
admin.site.register(Cliente)
from .models.servicio import Servicio
admin.site.register(Servicio)

# Register your models here.
