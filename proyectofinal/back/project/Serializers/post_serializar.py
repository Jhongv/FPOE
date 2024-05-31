from rest_framework import serializers
from api.models.post import Post
<<<<<<<< HEAD:proyectofinal/back/project/Serializers/post_serializer.py

class PostSerializers(serializers.ModelSerializer):
========
class PostSerializers(serializers.ModelSerializer): #Librerias
>>>>>>>> nr:proyectofinal/back/project/Serializers/post_serializar.py
    class Meta:
        model = Post  
        exclude = ['is_removed', 'created', 'modified']