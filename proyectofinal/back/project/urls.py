"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views.Cliente_view import *
from .views.Servicio_view import *
from .views.post_view import *
app_name= 'api'
#Corrigiendo una modificacion
urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/post', Post_APIView.as_view()), 
    path('v1/post/<int:pk>/', Post_APIView_Detail.as_view()),
    path('v1/cliente', Cliente_APIView.as_view()), 
    path('v1/cliente/<int:pk>/', Cliente_APIView_Detail.as_view()),
    path('v1/servicio', Servicio_APIView.as_view()), 
    path('v1/servicio/<int:pk>/', Servicio_APIView_Detail.as_view()),
    
]
