from django.contrib import admin
from django.urls import path
from .views.Cliente_view import Cliente_APIView, Cliente_APIView_Detail
from .views.Servicio_view import Servicio_APIView, Servicio_APIView_Detail
from .views.post_view import Post_APIView, Post_APIView_Detail

app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/post', Post_APIView.as_view()), 
    path('v1/post/<int:pk>/', Post_APIView_Detail.as_view()),
    path('v1/cliente', Cliente_APIView.as_view()), 
    path('v1/cliente/<int:pk>/', Cliente_APIView_Detail.as_view()),
    path('v1/servicio', Servicio_APIView.as_view()), 
    path('v1/servicio/<int:pk>/', Servicio_APIView_Detail.as_view()),
]
