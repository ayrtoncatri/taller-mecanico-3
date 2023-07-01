from django.urls import path
from .views import principal, nosotros, galeria, formulario, api, tienda, productos, exit, registro, add_producto, listar_productos, update_producto, delete_producto

urlpatterns = [
    path('', principal, name="principal"),
    path('nosotros', nosotros, name="nosotros"),
    path('galeria', galeria, name="galeria"),
    path('formulario', formulario, name="formulario"),
    path('api', api, name="api"),
    path('tienda', tienda, name="tienda"),
    path('productos/', productos, name="productos"),
    path('logout/', exit, name="exit"),
    path('registro/', registro, name="registro"),
    path('add_producto/', add_producto, name="add_producto"),
    path('listar_productos/', listar_productos, name="listar_productos"),
    path('update_producto/<id>/', update_producto, name="update_producto"),
    path('delete_producto/<id>/', delete_producto, name="delete_producto"),
]