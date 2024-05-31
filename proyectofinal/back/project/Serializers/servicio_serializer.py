from rest_framework import serializers
from api.models.servicio import Servicio #Si algo falla importemos mejor back.api.models.servicio import Servicio
class ClaseServicioSerializers(serializers.ModelSerializer):
    class Meta:
        model=Servicio
        fields='__all__'