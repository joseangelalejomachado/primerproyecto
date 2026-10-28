from django.db import models

# Create your models here.
# Cada clase corresponde a una tabla, cada atributo de la clase es una columna y cada instancia de la clase es una fila
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=60) 
    # En CharField es obligatoria la longitud máxima. Equivale al varchar
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField()