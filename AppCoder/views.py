from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from AppCoder.models import Persona
# Create your views here.

def persona(self):

    persona = Persona(nombre = "Pepe",apellido = "Perez" ,edad = "20")
    persona2 = Persona(nombre = "Juan",apellido = "Gonzalez" ,edad = "23")
    persona3= Persona(nombre = "Carla",apellido = "Sanchez" ,edad = "20")
    persona.save()
    persona2.save()
    persona3.save()
    text= f"Hola soy: {persona.nombre} {persona.apellido} y mi edad es : {persona.edad}, Hola soy: {persona2.nombre} {persona2.apellido} y mi edad es : {persona2.edad} , Hola soy: {persona3.nombre} {persona3.apellido} y mi edad es : {persona3.edad}"
    return HttpResponse(text)

