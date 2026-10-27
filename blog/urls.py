from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal' ),
    path('secundario', views.secundario, name='secundario'),
    # La estructura es: url(sobre blog en este caso), views.funcion
    # donde la función debe estar declarada en el views.py de la aplicación (en este caso blog)
]
