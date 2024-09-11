from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormularioVuelos
from .models import Vuelo

def inicio(request):
    return render(request, 'Vuelos/inicio.html')

def registrar_vuelo(request):
    if request.method == 'POST':
        form = FormularioVuelos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vuelo')
    else:
        form = FormularioVuelos()
    return render(request, 'Vuelos/registrar_vuelo.html', {'form': form})

def lista_vuelo(request):
    vuelos = Vuelo.objects.all().order_by('price')
    return render(request, 'Vuelos/lista_vuelo.html', {'vuelos': vuelos})

