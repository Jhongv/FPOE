from django.contrib import admin
from .models.post import Post
admin.site.register(Post)
from .models.persona import Persona
admin.site.register(Persona)

# Register your models here.
