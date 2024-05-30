from rest_framework.response import Response
from rest_framework.views import APIView
from ..Serializers.cliente_serializer import *
from api.models.cliente import Cliente
from rest_framework import status

from django.http import Http404
#Corriginendo una modificacion
#Cambiar esto por lo de la clase

from django.http import Http404, JsonResponse


class Cliente_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Cliente.objects.all()
        peso = self.request.query_params.get('peso')
        if peso is not None:
            queryset = queryset.filter(peso=peso)
        serializer = ClaseSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ClaseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Cliente_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = ClaseSerializers(post)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = ClaseSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)