from django.contrib import admin
from .models.post import Post
admin.site.register(Post)

from .models.cicla import Cicla
admin.site.register(Cicla)
