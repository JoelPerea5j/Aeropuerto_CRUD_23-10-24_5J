from django.shortcuts import render
from .models import Aviones
# Create your views here.
def ListadoAviones(request):
    losAviones=Aviones.objects.all()
    return render(request,"gestionarAviones.html",{"MisAviones":losAviones})
