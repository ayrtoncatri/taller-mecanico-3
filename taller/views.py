from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from taller.models import Producto
from taller.carrito import Carrito

from taller.forms import CustomUserCreationForm, ProductoForm
from django.contrib import messages


# Create your views here.

def principal(request):
    return render(request, 'taller/principal.html')

def nosotros(request):
    return render(request,'taller/nosotros.html')

def galeria(request):
    return render(request, 'taller/galeria.html')

def formulario(request):
    return render(request, 'registration/formulario.html')

def api(request):
    return render(request, 'taller/api.html')

def tienda(request):
    return render(request, "taller/tienda.html")

#CRUD 2

def add_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Exitosamente")
            return redirect(to="productos")
        else:
            data["form"] = formulario

    return render(request, 'taller/producto/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all()

    data = {
        'productos': productos

    }
    return render(request, 'taller/producto/listar.html', data)

def update_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Exitosamente")
            return redirect(to="productos")
        data["form"] = formulario

        

    return render(request, 'taller/producto/modificar.html', data)


def delete_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="productos")

# CRUD
# def registrarProducto(request):
#     nombre = request.POST['txtNombre']
#     categoria = request.POST['txtCategoria']
#     precio = request.POST['numPrecio']

#     producto = Producto.objects.create(
#         nombre=nombre, categoria=categoria, precio=precio)

#     return redirect('productos')

# def edicionProducto(request, id):
#     producto = Producto.objects.get(id=id)
#     return render(request, "taller/edicionProducto.html", {"producto": producto})

# def editarProducto(request, id):
#     nombre = request.POST['txtNombre']
#     categoria = request.POST['txtCategoria']
#     precio = request.POST['numPrecio']

#     producto = Producto.objects.get(id=id)
#     producto.nombre = nombre
#     producto.categoria = categoria
#     producto.precio = precio
#     producto.save()

#     return redirect('productos')

# def eliminacionProducto(request, id):
#     producto = Producto.objects.get(id=id)
#     producto.delete()

#     return redirect('productos')

@login_required
def productos(request):
    listaProductos = Producto.objects.all()
    return render(request, "taller/productos.html", {"productos": listaProductos})

def exit(request):
    logout (request)
    return redirect('principal')

# Para registrarse
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('principal')
    return render(request, 'registration/formulario.html', data)

# Para navegar en la tienda
@login_required
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "taller/tienda.html", {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")