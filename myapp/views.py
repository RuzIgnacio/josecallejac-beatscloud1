from django.shortcuts import render

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def acceder(request):
    return render(request, 'paginas/acceder.html')

def registrar(request):
    return render(request, 'paginas/registrar.html')

def catalogo(request):
    return render(request, 'paginas/catalogo.html')
