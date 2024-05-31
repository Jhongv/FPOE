from django.contrib import admin
from django.urls import path
from api.views import *
from .views.post_views import *
from .views.Cliente_view import *
from .views.Servicio_view import *


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

