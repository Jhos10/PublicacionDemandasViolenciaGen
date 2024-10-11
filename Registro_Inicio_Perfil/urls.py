from django.urls import path
from .views import *
urlpatterns = [path('RegistroUsuario/', registroUsuario, name='registroUsuario')]