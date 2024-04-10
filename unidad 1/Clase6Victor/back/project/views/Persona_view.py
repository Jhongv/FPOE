from rest_framework.response import Response
from rest_framework.views import APIView
from ..Serializers.persona_serializer import ClaseSerializers
from api.models.persona import Persona
from rest_framework import status
from django.http import Http404

#Cambiar esto por lo de la clase
class Persona_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        post = Persona.objects.all()
        serializer = ClaseSerializers(post, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ClaseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Persona_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
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