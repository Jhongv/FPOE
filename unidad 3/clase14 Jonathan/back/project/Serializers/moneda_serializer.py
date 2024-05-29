from rest_framework import serializers
from api.models.moneda import Moneda
class ClaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields=["id", "valor", "peso", "tamaño", "color"]