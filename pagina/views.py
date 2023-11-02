from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Material
from .forms import MaterialForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/index.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

@login_required
def materiales(request):
    materiales = Material.objects.all()
    return render(request, 'materiales/index.html', {'materiales': materiales})
@login_required
def crear(request):
    formulario = MaterialForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('materiales')
    return render(request, 'materiales/crear.html', {'formulario': formulario})
@login_required
def editar(request, id):
    material = Material.objects.get(id=id)
    formulario = MaterialForm(request.POST or None, request.FILES or None, instance=material)
    return render(request, 'materiales/editar.html', {'formulario': formulario})
@login_required
def eliminar(request, id):
    material = Material.objects.get(id=id)
    material.delete()
    return redirect('materiales')

def exit(request):
    logout(request)
    return redirect('inicio')