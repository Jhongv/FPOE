from rest_framework import serializers
from api.models.servicio import Servicio

class ClaseServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Servicio
        fields='__all__'