from django.db import models

# Create your models here.
# Cada clase corresponde a una tabla, cada atributo de la clase es una columna y cada instancia de la clase es una fila
class Autor(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE, # Si se borra un autor, se borran todos sus posts
        related_name="posts",    # Related_name es el nombre que se le da a la relación inversa, es decir, desde un autor se puede acceder a sus posts con autor.posts.all()
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="posts")
    # En CharField es obligatoria la longitud máxima. Equivale al varchar
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField()

    def __str__(self):
        return f"{self.titulo} ({self.autor})"