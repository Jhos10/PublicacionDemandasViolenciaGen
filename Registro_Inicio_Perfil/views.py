import random
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import PublicacionDenuncia,User
from django.db.models import Q

# Create your views here.

def generarCasosDenuncias():

  nombres_victima = ["Valentina", "Camila", "Daniela", "Sofía", "Mariana", "Laura", "Isabella", "Gabriela", "Lucía", "Natalia", "Andrea", "Sara", "Juliana", "Paula", "María", "Antonia", "Martina", "Carolina", "Ángela", "Victoria"]

  apellidos_victima = ["Gómez", "López", "Rodríguez", "Pérez", "Martínez", "González", "Hernández", "Ramírez", "Torres", "Vargas", "Romero", "Díaz", "Moreno", "Muñoz", "Jiménez", "Ortiz", "Cruz", "Reyes", "Ríos", "Castro"]

  direccion = ["Avenida 30 de Agosto No 68 - 125 Barrio Cañaveral",
  "Calle 71 No 26 - 57 Barrio Cuba", 
  "Avenida Las Américas No 53 - 20 Barrio Avenida Sur", 
  "Avenida 30 de Agosto No 42 - 75 Barrio Maraya", 
  "Carrera 8 Bis No 30 B - 49 Barrio Centro", 
  "Avenida 30 de Agosto No 30 - 30 Local 27 Barrio Repuestos", 
  "Carrera 7 No 25 - 18 Barrio Centro", 
  "Carrera 9 No 21 - 03 Barrio Centro", 
  "Carrera 10 No 16 - 60 Barrio C. Cultural Lucy Tejeda", 
  "Avenida Circunvalar No 10 - 26 Barrio Circunvalar", 
  "Calle 16 No 6 - 34 Barrio Centro", 
  "Carrera 15A No 148 - 37 Barrio La Julita", 
  "Carrera 5 No 16 - 63 Barrio San Nicolás", 
  "Calle 69 No 25 - 08 Barrio Cuba", 
  "Carrera 2 No 23 - 29 Barrio San Joaquín", 
  "Carrera 13 No 15 - 35 Barrio El Centro", 
  "Calle 21 No 4 - 23 Barrio Pinares", 
  "Carrera 3 No 16 - 54 Barrio San Fernando", 
  "Calle 50 No 20 - 05 Barrio Álamos", 
  "Carrera 6 No 23 - 33 Barrio Corales"]

  ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Bucaramanga", "Manizales", "Santa Marta"]

  tipos_documento = ['CC', 'TI', 'Pasaporte']

  grado_violencia = ['Bajo', 'Moderado', 'Alto']

  descripciones = ["El agresor controlaba las finanzas de la víctima, impidiéndole acceder a sus propios recursos. Además, ejercía amenazas constantes de violencia física para mantener el control. La víctima vivía en un constante estado de estrés y miedo. No tenía libertad financiera ni personal.",
  "Durante varios años, la víctima fue objeto de insultos, humillaciones y golpes. Los episodios de violencia eran frecuentes, causando graves secuelas emocionales y físicas. La víctima desarrolló depresión y ansiedad. El agresor continuaba negando cualquier responsabilidad.",
  "El agresor ejerció violencia psicológica mediante constantes intimidaciones y amenazas. El ambiente en el hogar era de control total, generando temor en la víctima. La manipulación emocional fue devastadora para su bienestar. El aislamiento era parte de la táctica del agresor.",
  "La víctima fue agredida físicamente en varias ocasiones, sufriendo fracturas y lesiones graves. Los ataques eran repentinos y sin motivo aparente. A pesar del daño físico, la víctima temía denunciar. El agresor la manipulaba psicológicamente para que no buscara ayuda.",
  "El agresor forzó a la víctima a mantener relaciones sexuales en contra de su voluntad. Además, la insultaba y degradaba constantemente, afectando su autoestima. La víctima se sentía atrapada y sin salida. El abuso sexual se repitió en varias ocasiones sin castigo.",
  "En varias ocasiones, el agresor la golpeó en presencia de sus hijos, aumentando el terror en el hogar. Los niños también fueron testigos de las amenazas. La violencia generaba un ambiente de miedo constante. La víctima no se sentía segura en su propia casa.",
  "El agresor la acosaba constantemente, vigilando cada uno de sus movimientos. Restringía su libertad para salir de casa y la castigaba con violencia física y emocional. La víctima se sentía atrapada bajo un control absoluto. No podía salir sin su permiso.",
  "La víctima sufrió violencia emocional continua, siendo insultada y descalificada constantemente. El agresor aprovechaba cada oportunidad para humillarla, tanto en público como en privado. Su autoestima estaba destruida. Vivía en una espiral de abuso verbal.",
  "El agresor utilizaba amenazas de muerte para manipular y controlar a la víctima. Cada vez que intentaba buscar ayuda, él la intimidaba con represalias. Además, la agredía físicamente en diversas ocasiones. La víctima temía por su vida y no encontraba salida.",
  "El agresor sometió a la víctima a múltiples agresiones físicas a lo largo del tiempo. Las lesiones visibles eran la prueba de los constantes ataques. También la amenazaba para evitar que denunciara. El silencio impuesto por el miedo hacía que el abuso continuara."
  ]

  nombres_Agresores = ["Santiago", "Mateo", "Sebastián", "Alejandro", "Diego", "Samuel", "Tomás", "Lucas", "David", "Gabriel", "Emiliano", "Juan", "Daniel", "Carlos", "Miguel", "Andrés", "Nicolás", "Joaquín", "Hugo", "Ricardo"]
  antecedentes_Penales = ["Homicidio", "Robo agravado", "Tráfico de drogas", "Violencia intrafamiliar", "Fraude", "Lavado de activos", "Conspiración criminal", "Extorsión", "Secuestro", "Agresión sexual"]

  for x in range(51):
    PublicacionDenuncia.objects.create(nombreVictima = nombres_victima[random.randint(0,len(nombres_victima)-1)], primerApellidoVictima = apellidos_victima[random.randint(0,len(apellidos_victima)-1)],segundoApellidoVictima = apellidos_victima[random.randint(0,len(apellidos_victima)-1)], edadVictima = random.randint(15,80), tipoDocumentoVictima = tipos_documento[random.randint(0,len(tipos_documento)-1)], numeroDocumentoVictima = random.randint(1000000000, 2000000000), ciudadNacimientoVictima = ciudades[random.randint(0, len(ciudades)-1)], ciudadRecidenciaVictima = ciudades[random.randint(0, len(ciudades)-1)],nombreAgresor = nombres_Agresores[random.randint(0, len(nombres_Agresores)-1)],  primerApellidoAgresor = apellidos_victima[random.randint(0,len(apellidos_victima)-1)], segundoApellidoAgresor = apellidos_victima[random.randint(0,len(apellidos_victima)-1)], tipoDocumentoAgresor = tipos_documento[random.randint(0,len(tipos_documento)-1)], numeroDocumentoAgresor = random.randint(1000000000, 2000000000), ciudadNacimientoAgresor = ciudades[random.randint(0, len(ciudades)-1)],ciudadResidenciaAgresor = ciudades[random.randint(0, len(ciudades)-1)], antecedentesPenalesAgresor = antecedentes_Penales[random.randint(0,len(antecedentes_Penales)-1)], edadAgresor =  random.randint(15,80), fecha = f'{random.randint(2000,2025)}-{random.randint(1,12)}-{random.randint(1,29)}', descripcion = descripciones[random.randint(0,len(descripciones)-1)], prevenciones = '', ubicacion = direccion[random.randint(0, len(direccion)-1)])


def registroUsuario(request):
  if request.method == 'GET':
    HttpResponse('Estas en el registro de usuario')

  if request.method == 'POST':
    if request.POST["PasswordUno"] == request.POST["PasswordDos"]:
      usuario = User.objects.filter(Q(email = request.POST["Email"]) | Q(username = request.POST["Username"]))
      if usuario.exists():

        HttpResponse("Usuario redirigido al perfil")

      else:

        User.objects.create(username = request.POST['Username'], password = request.POST['PassswordUno'], email = request.POST['Email'])

        usuario = authenticate(username = request.POST["Username"], password = request.POST["PasswordUno"])
        login(User, usuario)
        # redirect()
        HttpResponse("Ingreso el usuario a su nuevo perfil de usuario")

def inicioSesion(request):
  if request.method == 'GET':
    usuario = authenticate(username = request.POST["Username"], password = request.POST["Password"])
    if usuario is None:
      return None
    else:
      login(User, usuario)
      return None
