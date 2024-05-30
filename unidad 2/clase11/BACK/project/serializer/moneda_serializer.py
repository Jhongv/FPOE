from rest_framework import serializers
from api.models.moneda import Moneda
class MonedaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        exclude = ["id"]
        
     