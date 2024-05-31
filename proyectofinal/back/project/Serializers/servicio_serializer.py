from rest_framework import serializers

from api.models.servicio import Servicio
from api.models.servicio import Servicio #Si algo falla importemos mejor back.api.models.servicio import Servicio
class ClaseServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Servicio
        fields='__all__'