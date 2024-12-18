from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Invernadero
import json

# Create your views here.

@csrf_exempt
def guardarDatosInvernadero(request):
    if request.method == "POST":
        temperatura = request.POST.get('Temperatura')
        humedad = request.POST.get('Humedad')
        luz = request.POST.get('Luz')

        Invernadero.objects.create(Temperatura=temperatura, Humedad=humedad,  Luz =luz)

        return HttpResponseRedirect('listarDatos/')
    return render(request, "registrarDatos.html")



def listarDatosInvernadero(request):
    if request.method == "GET":
        # Ordena los datos de menor a mayor por el ID
        datos = Invernadero.objects.all().order_by("id")
        return render(request, "listarDatos.html", {'datos': datos})
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def editarDatosInvernadero(request, id):
    # Recupera el objeto o lanza un error 404 si no existe
    dato = get_object_or_404(Invernadero, id=id)

    if request.method == "POST":
        # Actualiza los datos con la información del formulario
        dato.Temperatura = request.POST.get('Temperatura')
        dato.Humedad = request.POST.get('Humedad')
        dato.Luz = request.POST.get('Luz')
        dato.save()
        return redirect('listarDatos')  # Redirige a la lista de datos

    # Si es GET, renderiza el formulario con los datos actuales
    return render(request, 'editarDatos.html', {'dato': dato})


def eliminarDatosInvernadero(request, id):
    try:
        # Buscar el objeto por su id y eliminarlo
        dato = Invernadero.objects.get(id=id)
        dato.delete()
        # Redirigir a la página listarDatos en registrarDatos
        return HttpResponseRedirect('/Invernadero/registrarDatos/listarDatos/')
    except Invernadero.DoesNotExist:
        # Si no se encuentra el dato, redirigir a la lista con un error
        return HttpResponseRedirect('/Invernadero/registrarDatos/listarDatos/?error=notfound')