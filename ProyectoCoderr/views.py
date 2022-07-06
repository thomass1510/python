from django.template import loader
from django.http import HttpResponse
from AppCoder.models import Persona
from AppCoder.views import persona


def template(self):

    nombre = Persona.nombre
    apellido = Persona.apellido
    edad = Persona.edad

    diccionario = {"nombre": nombre, "apellido": apellido, "edad": edad}

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
