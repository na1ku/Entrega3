from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Holiwi mundooo")

def probando_template(self):
    # mi_template = open("Entrega3/Proyecto1/templates/template1.html")
        # plantilla = Template(mi_template.read())
    # mi_template.close()
    # contexto = Context()
    # documento = plantilla.render(contexto)
    diccionario = {"nombre_persona": "Nicolas", "apellido_persona": "Jimenez"}   
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)