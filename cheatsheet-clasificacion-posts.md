# Cheatsheet: añadir una clasificación a los posts

## Dónde se hace cada paso

| Paso                       | Archivo                                                          |
|----------------------------|------------------------------------------------------------------|
| 1. Crear el modelo         | `blog/models.py`                                                 |
| 2. Relacionarlo con `Post` | `blog/models.py`                                                 |
| 3. Crear migraciones       | `blog/migrations/`, mediante `manage.py`                         |
| 4. Registrar en admin      | `blog/admin.py`                                                  |
| 5. Crear vista de listado  | `blog/views.py`                                                  |
| 6. Crear vista filtrada    | `blog/views.py`                                                  |
| 7. Añadir URLs             | `blog/urls.py`                                                   |
| 8. Crear plantilla         | `blog/templates/blog/`                                           |
| 9. Añadir enlaces          | `principal.html`, `autores.html`, `categoria.html` y `base.html` |
| 10. Probar el flujo        | Panel `/admin`, navegador y comandos `manage.py`                 |

## Aplicado a una categoría

```text
blog/models.py
    Modelo Categoria + relación Post.categoria

blog/migrations/
    makemigrations + migrate

blog/admin.py
    register(Categoria)

blog/views.py
    categoria(request, pk)
    Post.objects.filter(categoria=categoria)

blog/urls.py
    path('categoria/<int:pk>', ...)

blog/templates/blog/categoria.html
    Mostrar posts filtrados

principal.html / base.html
    Enlaces hacia la categoría
```

## Comandos

Desde la carpeta raíz del proyecto:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Fórmula corta

> **models.py → migrations → admin.py → views.py → urls.py → templates/blog/**
