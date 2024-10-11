from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Registro_Inicio_Perfil.models import PublicacionDenuncia
# Create your views here.
def paginaPrincipal(request):
  publicacionesDenuncias = PublicacionDenuncia.objects.all()
  return render(request, 'paginaPrincipal.html', {'publicacionesDenuncias': publicacionesDenuncias})

