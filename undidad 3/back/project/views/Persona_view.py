import json
import asyncio
import aiofiles
import time
import schedule
from rest_framework.response import Response
from rest_framework.views import APIView
from ..Serializers.persona_serializer import *
from api.models.persona import Persona
from rest_framework import status
from django.http import Http404, JsonResponse

class Persona_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Persona.objects.all()
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

class Persona_API_serializer(APIView):
    def exportarPersona(request):
        personas = Persona.objects.all()
        serializer = ClaseSerializers(personas, many=True)
        data = serializer.data

        with open('personas.json', 'w') as f:
            json.dump(data, f, indent=4)

        return JsonResponse({'mensaje': 'Datos exportados correctamente'})

# Función asíncrona para guardar datos en un archivo
from asgiref.sync import sync_to_async

async def guardar_datos_asincrono():
    while True:
        personas = await sync_to_async(Persona.objects.all)()
        serializer = ClaseSerializers(personas, many=True)
        data = serializer.data

        async with aiofiles.open('personas.json', 'w') as f:
            await f.write(json.dumps(data, indent=4))
        
        print("Datos guardados correctamente de manera asíncrona")
        await asyncio.sleep(60)  # Esperar 60 segundos antes de la próxima sincronización
# Esperar 60 segundos antes de la próxima sincronización

# Función para ejecutar el bucle de eventos de asyncio
def ejecutar_asyncio():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(guardar_datos_asincrono())
    loop.run_forever()


# Programar la tarea de sincronización cada cierto tiempo usando schedule
def programar_tarea():
    schedule.every(1).minutes.do(ejecutar_asyncio)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Iniciar la ejecución de la sincronización
import threading
threading.Thread(target=programar_tarea, daemon=True).start()
