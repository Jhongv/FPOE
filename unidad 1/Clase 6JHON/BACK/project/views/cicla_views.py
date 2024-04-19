from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializer.cicla_serializer import CiclaSerializers  # Corregido el nombre del serializador
from api.models.cicla import Cicla  # Corregido el modelo Cicla
from rest_framework import status
from django.http import Http404

class Cicla_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        cicla_objects = Cicla.objects.all()  # Cambiado el nombre de la variable para mayor claridad
        serializer = CiclaSerializers(cicla_objects, many=True)  # Corregido el nombre del serializador
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CiclaSerializers(data=request.data)  # Corregido el nombre del serializador
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Cicla_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Cicla.objects.get(pk=pk)  # Corregido el modelo Cicla
        except Cicla.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = CiclaSerializers(post)  # Corregido el nombre del serializador
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = CiclaSerializers(post, data=request.data)  # Corregido el nombre del serializador
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
