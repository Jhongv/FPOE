from django.contrib import admin
from .models.post import Post
from .models.cliente import Cliente
from .models.servicio import Servicio
admin.site.register(Post)
admin.site.register(Cliente)
admin.site.register(Servicio)


# Register your models here.
