import json
import asyncio
import aiofiles
import time
import schedule
from rest_framework.response import Response
from rest_framework.views import APIView
<<<<<<<< HEAD:undidad 3/clase 14/back/project/views/moneda_views.py
from ..Serializers.moneda_serializer import ClaseSerializers
from api.models.moneda import Moneda
========
from ..Serializers.persona_serializer import *
from api.models.persona import Persona
>>>>>>>> fda2f0fc34e6455cc991a3a59752dc18864c3542:unidad 3/clase14victor/back/project/views/Persona_view.py
from rest_framework import status

from django.http import Http404
#Corriginendo una modificacion
#Cambiar esto por lo de la clase
<<<<<<<< HEAD:undidad 3/clase 14/back/project/views/moneda_views.py
class Moneda_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset=Moneda.objects.all()
        peso= self.request.query_params.get('peso')
========

from django.http import Http404, JsonResponse


class Persona_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Persona.objects.all()
        peso = self.request.query_params.get('peso')
>>>>>>>> fda2f0fc34e6455cc991a3a59752dc18864c3542:unidad 3/clase14victor/back/project/views/Persona_view.py
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
<<<<<<<< HEAD:undidad 3/clase 14/back/project/views/moneda_views.py
class Moneda_APIView_Detail(APIView):
========

class Persona_APIView_Detail(APIView):
>>>>>>>> fda2f0fc34e6455cc991a3a59752dc18864c3542:unidad 3/clase14victor/back/project/views/Persona_view.py
    def get_object(self, pk):
        try:
            return Moneda.objects.get(pk=pk)
        except Moneda.DoesNotExist:
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

