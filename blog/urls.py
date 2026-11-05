from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal' ),
    path('secundario', views.secundario, name='secundario'),
    path('<int:pk>', views.detalle_post, name='detalle_post'),
    path('autores', views.autores, name='autores'),
    path('autor/<int:pk>', views.entradas_autor, name='entradas_autor'),
    path('categoria/<int:pk>', views.categoria, name='categoria')
    # La estructura es: url(sobre blog en este caso), views.funcion
    # donde la función debe estar declarada en el views.py de la aplicación (en este caso blog)
]
