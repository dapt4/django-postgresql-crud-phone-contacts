from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dato

# Create your views here.
def index(request):
    list_numbers = Dato.objects.all()
    return render(request, 'index.html', {"list_numbers": list_numbers})

def create(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        numero = request.POST["numero"]
        dato = Dato(nombre=nombre, numero=numero)
        dato.save()
        return redirect("/")
    return render(request, 'create.html')

def delete(request, dato_id):
    dato = Dato.objects.get(dato_id=dato_id)
    dato.delete()
    return redirect('/')

def edit(request, id):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        numero = request.POST['numero']
        dato = Dato.objects.get(dato_id=id)
        dato.nombre, dato.numero = nombre, numero
        dato.save()
        return redirect('/')
    dato = Dato.objects.get(dato_id=id)
    return render(request, 'edit.html', {'dato': dato})
    
