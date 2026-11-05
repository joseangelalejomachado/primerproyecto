from django.contrib import admin
from .models import Autor, Post, Categoria

# Register your models here.

admin.site.register(Autor)
admin.site.register(Post)
admin.site.register(Categoria)