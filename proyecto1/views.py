from  django.http import HttpResponse
from django.template import Template, Context
import datetime #importar modulo para fecha, sirve importar los 
from django.template import loader #sirve para poder cargar (template) platillas
#para que el editor te ayude el asistente. o puede ser
from django.template.loader import get_template #util cunado se van a cargar muchas plantillas
#en views solo seria get_template(nombre de la plantilla)
from django.shortcuts import render #nos ahorramos la linea de redner en la plantillas (ver cambio de salud0_3 a saludo_4)


def saludo(request): #primera vista
    #Utilizar codigo Html para programar, vistas tamaños, colores. etc
    #tripe comilla para indicar que todas las lineas pertenecen a la misma cadena
    #La siuiente forma no es la adecuada, se deben utilizar plantillas
    titulo="""<html>  
    <body>
    <h1>
    Hola Johnny, sigue asi vas muy bien 
    </h1>
    </body>
    </html>"""
    
    return HttpResponse(titulo)
    

def fechayhora(request):
    fecha_actual=datetime.datetime.now() #datetime.now devuelve fecha y hora actuales

    titulo="""<html>  
    <body>
    <h2>
    la hora y la fecha son %s
    </h2>
    </body>
    </html>""" % fecha_actual  

    return HttpResponse(titulo)


def edad(request,edadactual,agno):
    #edadactual=25
    periodo=agno-2019
    edadfutura=edadactual+periodo
    documento="""<html>  
    <body> 
    <h2> 
    en el año %s tendras %s años  
    <body> 
    <h2> 
    <html>""" %(agno,edadfutura)
    
    return HttpResponse(documento)

#*************PLANTILLAS*************************#
    
#plantillas:cadenas de texto (HTML casi siempre) sirven para saparar la parte 
#logica de nuestro proyecto, (los datos,
#lo que el usuario ve) del formato.

#Como se usan: 
# importar la clase template y la clase context
# 1: Crear objeto de tipo template: lea los documetnos de html desde la carpeta externa
#plt=tenplate(doc_externo.read())
#2 crear un contexto: datos adicionales que puede usar el template
#ctx=context()
#3 Renderizar el objeto template 
#documento=plt.render(ctx)

#Ejemplo de Primera vista (primera funcion arriba) con plantilla

def saludo_1(request): 
    doc_externo=open("C:/Users/Johnny/Desktop/Proyectos Django/proyecto1/proyecto1/plantillas/miplantilla.html") #abirir documento
    plt=Template(doc_externo.read()) #cargar el documento en plt

    doc_externo.close()    #cerrar documento 

    #contexto vacio porque el cofigo html es muy basico

    ctx=Context() 
    #renderizar
    titulo = plt.render(ctx)
    
    return HttpResponse(titulo)

class Persona(object):
    def __init__(self, nombre, apellido):

        self.nombre=nombre
        self.apellido=apellido 

#***************************************************
#Uso de variables en plnatillas
def saludo_2(request): 
    p1=Persona("Johnny","Jojoa")

    #uso de variables en las plantillas
    #Acceso a objetos y y propiedades desde plantillas
    #   --uso de diccioarios en contexto
    #  
    
    #nombre="Juan"  #Variable para utiliar en la plnatilla 
    #apellido="Martinez" #pueden ir aqui o directamente en el contexto

    fecha_hoy=datetime.datetime.now() #variable para poner fecha y hora actuales

    servicios1=["metronomo","rutinas","productos","contacto"]

    doc_externo=open("C:/Users/Johnny/Desktop/Proyectos Django/proyecto1/proyecto1/plantillas/miplantilla.html") #abirir documento
    plt=Template(doc_externo.read()) #cargar el documento en plt

    doc_externo.close()    #cerrar documento 

    #contexto vacio porque el codigo html es muy básico

    ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":fecha_hoy,"servicios": servicios1 }) # el contexto recibe diccionarios, estos permiten hacer uso de variables
    #nombre persona es la clave indicativa del diccionarios y el valor es nombre lo que se ha almacenado en la variable nombre
    #"temas"para pasarle a la plantilla una lista     
   
    #renderizar
    titulo = plt.render(ctx)
    
    return HttpResponse(titulo)     


#*******************************************************
#la siguiente es la forma mas optima de cargar plantillas
# 1. En el archivo setting se decimos a Django (a nuestro proyecto) donde estan
# las plantillas - Dentro de Settings- TEMPLATES - DIRS [La ruta donde estan las plantillas]
def saludo_3(request): 

    cargar_plantilla=loader.get_template("miplantilla.html")
    p1=Persona("Johnny","Jojoa")

    fecha_hoy=datetime.datetime.now() 

    servicios1=["metronomo","rutinas","productos","contacto"]

    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":fecha_hoy,"servicios": servicios1 }) # el contexto recibe diccionarios, estos permiten hacer uso de variables

    titulo = cargar_plantilla.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":fecha_hoy,"servicios": servicios1}) #con el metodo template se introduce en render directamente un diccionario
    
    return HttpResponse(titulo)     


    #*******MODULO_SHORTCUT********************
    #metodo_render 
    #render(requst(obligatorio)"nombre de la plantilla", diccionario(opcional) )   
def saludo_4(request): 

    #cargar_plantilla=loader.get_template("miplantilla.html")
    p1=Persona("Johnny","Jojoa")

    fecha_hoy=datetime.datetime.now() 

    servicios1=["metronomo","rutinas","productos","contacto"]

    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":fecha_hoy,"servicios": servicios1 }) # el contexto recibe diccionarios, estos permiten hacer uso de variables

    #titulo = cargar_plantilla.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":fecha_hoy,"servicios": servicios1}) #con el metodo template se introduce en render directamente un diccionario
    
    return render(request, "miplantilla.html", {"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":fecha_hoy,"servicios": servicios1})     


    #***********PLANTILLAS_INCRUSTADAS******************

     #1.crear otra plantilla para incrustar (plantilla_barra)
    #2. Determinar donde deseamos que aparezca la plantilla - En la plantilla General
    # por ejemplo para que aparezca arriba se pone despues del body de la plantila general ({% include "nombreplantilla" % })
    #Curso ccs para dar apariencia y barra funcional

