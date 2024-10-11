# from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PublicacionDenuncia(models.Model):
  # Atributos que representan una victima
  nombreVictima = models.CharField(default='Anonimo', max_length=50)
  primerApellidoVictima = models.CharField(default='Anonimo', max_length=50)
  segundoApellidoVictima = models.CharField(default='Anonimo', max_length=50)
  edadVictima = models.IntegerField(default=0)
  tipoDocumentoVictima = models.CharField(default='No tiene', max_length=50)
  numeroDocumentoVictima = models.CharField(default='No se sabe', max_length=50)
  ciudadNacimientoVictima = models.CharField(default='No esta definida', max_length=50)
  ciudadRecidenciaVictima = models.CharField(default='No esta definida', max_length=50)

  # Atributos del agresor
  nombreAgresor = models.CharField(default='Anonimo', max_length=50)
  primerApellidoAgresor = models.CharField(default='Anonimo', max_length=50)
  segundoApellidoAgresor = models.CharField(default='Anonimo', max_length=50)
  tipoDocumentoAgresor = models.CharField(default='No se especifica', max_length=50)
  numeroDocumentoAgresor = models.CharField(default='No se especifica', max_length=50)
  ciudadNacimientoAgresor = models.CharField(default='No se especifica', max_length=50)
  ciudadResidenciaAgresor = models.CharField(default='No se especifica', max_length=50)
  antecedentesPenalesAgresor = models.TextField(default='No se conocen', max_length=50)
  edadAgresor = models.IntegerField(default=0)
  
  # Atributos de la denuncia
  titulo = models.CharField(default='No tiene titulo', max_length=50)
  # gradoDeViolencia = models.IntegerField(default=0)
  fecha = models.DateField(default=None)
  descripcion = models.TextField(default='No hay suficiente informacion para generar una descripcion', max_length=1000)
  prevenciones = models.TextField(default='No estan disponibles', max_length=1000)
  ubicacion = models.CharField(default='No se conoce la ubicacion de la demanda', max_length=50)
  # tipoDeDenuncia = models.CharField(default='No se especifica', max_length=20) 
  def __str__(self) -> str:
    return str(self.titulo)
  