from django.contrib import admin
from .models.post import Post
admin.site.register(Post)

from.models.moneda import Moneda
admin.site.register(Moneda)