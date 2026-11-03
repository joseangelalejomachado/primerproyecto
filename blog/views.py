from django.shortcuts import render
from .models import Post

# Create your views here.
def principal(request):
    # Mostrando todos los objetos de la tabla Post (entradas del blog)
    posts = Post.objects.all()
    print(f"\nMostrando todos los posts: ")

    # Diccionario de los objetos de la tabla Post
    contexto = {
        'posts': posts,
    }

    print(posts)
    # Mostrando los objetos con un id especifico
    post1 = Post.objects.get(id=1)
    print(f"\nMostrando los objetos con id especifico 1:")
    print(post1)
    # Mostrando objetos que en el campo contengan "mejor"
    post_mejor = Post.objects.filter(cuerpo__contains='mejor')
    print(f"\nMostrando posts que contienen en cuerpo 'mejor':")
    print(post_mejor)
    # Mostrando objetos que en el título contengan "post"
    post_titulopost = Post.objects.filter(titulo__icontains='post')
    print(f"\nPost que en el título contienen 'post'")
    print(post_titulopost)
    return render(request, 'blog/principal.html', contexto)

# Función para llamar a una nueva vista
def secundario(request):
    return render(request, 'blog/secundario.html')