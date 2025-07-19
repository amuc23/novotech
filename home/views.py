from django.shortcuts import render

def home_view(request):
    return render(request, 'home/index.html')

def contacto(request):
    return render(request, 'contacto.html')

def maquinas(request):
    return render(request, 'maquinas.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')