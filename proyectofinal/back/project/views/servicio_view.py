from rest_framework.response import Response
from rest_framework.views import APIView
from ..Serializers.servicio_serializer import *
from api.models.servicio import Servicio
from rest_framework import status

from django.http import Http404
#Corriginendo una modificacion
#Cambiar esto por lo de la clase

from django.http import Http404, JsonResponse


class Servicio_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Servicio.objects.all()
        peso = self.request.query_params.get('peso')
        if peso is not None:
            queryset = queryset.filter(peso=peso)
        serializer = ClaseServicioSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ClaseServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Servicio_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = ClaseServicioSerializer(post)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = ClaseServicioSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)