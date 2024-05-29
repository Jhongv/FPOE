from rest_framework import serializers
from api.models.persona import Persona
class ClaseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields='__all__'