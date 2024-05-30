from rest_framework.response import Response
from rest_framework.views import APIView
from ..Serializers.moneda_serializer import ClaseSerializers
from api.models.moneda import Moneda
from rest_framework import status
from django.http import Http404

#Cambiar esto por lo de la clase
class Moneda_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset=Moneda.objects.all()
        peso= self.request.query_params.get('peso')
        if peso is not None:
            queryset=queryset.filter(peso=peso)
        serializer=ClaseSerializers(queryset, many=True)
        return Response(serializer.data)
        

    def post(self, request, format=None):
        serializer = ClaseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Moneda_APIView_Detail(APIView):
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