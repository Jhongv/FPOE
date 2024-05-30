from rest_framework import serializers
from api.models.cliente import Cliente

class ClaseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'