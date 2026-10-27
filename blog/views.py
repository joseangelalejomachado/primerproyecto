from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request, 'blog/principal.html')
# Función para llamar a una nueva vista
def secundario(request):
    return render(request, 'blog/secundario.html')