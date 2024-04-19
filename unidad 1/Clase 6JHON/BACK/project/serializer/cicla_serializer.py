from rest_framework import serializers
from api.models.cicla import Cicla
class CiclaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cicla
        exclude = ["id"]
        