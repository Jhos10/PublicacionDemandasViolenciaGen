from django.urls import path
from .views import *
urlpatterns = [
  path('', paginaPrincipal, name='paginaPrincipal')]