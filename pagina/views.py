from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Material, Cart, CartMaterial
from .forms import MaterialForm, MaterialSearchForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/index.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def servicios(request):
    return render(request, 'paginas/servicios.html')

def presupuesto(request):
    material = Material.objects.all()
    return render(request, 'paginas/presupuesto.html', {'material': material})

def add_to_budget(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    session_key = request.session.session_key

    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    cart, created = Cart.objects.get_or_create(session_key=session_key)

    try: 
        cart_material = CartMaterial.objects.get(cart=cart, material=material)
        cart_material.quantity += 1
        cart_material.save()
    except CartMaterial.DoesNotExist:
        CartMaterial.objects.create(cart=cart, material=material, quantity=1)

    return redirect('presupuesto')

def factura(request):
    session_key = request.session.session_key

    cart = Cart.objects.get(session_key=session_key)

    cart_material = CartMaterial.objects.filter(cart=cart)
    total = sum(item.material.precio * item.quantity for item in cart_material)

    return render(request, 'paginas/factura.html', {'cart_material': cart_material, 'total': total})

def remove_from_budget(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    session_key = request.session.session_key

    cart = Cart.objects.get(session_key=session_key)

    try:
        cart_material = CartMaterial.objects.get(cart=cart, material=material)
        if cart_material.quantity > 1:
            cart_material.quantity -= 1
            cart_material.save()
        else:
            cart_material.delete()
    except CartMaterial.DoesNotExist:
        pass

    return redirect('factura')

@login_required
def materiales(request):
    materiales = Material.objects.all()
    form = MaterialSearchForm(request.GET)

    if form.is_valid():
        search_term = form.cleaned_data['search_term']
        if search_term:
            materiales = materiales.filter(nombre__icontains=search_term)

    return render(request, 'materiales/index.html', {'materiales': materiales, 'form': form})
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