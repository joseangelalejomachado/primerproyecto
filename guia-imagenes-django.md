# Guía: subir y mostrar imágenes en Django

Esta guía aplica la tarea de añadir imágenes a los `Post` del proyecto.

- [Guía: subir y mostrar imágenes en Django](#guía-subir-y-mostrar-imágenes-en-django)
  - [Objetivo](#objetivo)
  - [1. Activar el entorno virtual](#1-activar-el-entorno-virtual)
  - [2. Instalar Pillow (solo para subir archivos)](#2-instalar-pillow-solo-para-subir-archivos)
  - [3. Elegir cómo guardar la imagen](#3-elegir-cómo-guardar-la-imagen)
    - [Opción A: subir la imagen al servidor](#opción-a-subir-la-imagen-al-servidor)
    - [Opción B: introducir una URL](#opción-b-introducir-una-url)
    - [Significado de las opciones](#significado-de-las-opciones)
  - [4. Crear y aplicar la migración](#4-crear-y-aplicar-la-migración)
  - [5. Configurar los archivos multimedia (solo para la opción A)](#5-configurar-los-archivos-multimedia-solo-para-la-opción-a)
    - [Diferencia entre ambos ajustes](#diferencia-entre-ambos-ajustes)
  - [6. Hacer públicas las imágenes durante el desarrollo (solo para la opción A)](#6-hacer-públicas-las-imágenes-durante-el-desarrollo-solo-para-la-opción-a)
  - [7. Mostrar la imagen en una plantilla](#7-mostrar-la-imagen-en-una-plantilla)
    - [Plantilla para la opción A: imagen subida](#plantilla-para-la-opción-a-imagen-subida)
    - [Plantilla para las dos opciones](#plantilla-para-las-dos-opciones)
  - [8. Subir una imagen o introducir una URL desde el admin](#8-subir-una-imagen-o-introducir-una-url-desde-el-admin)
  - [9. Comprobación completa](#9-comprobación-completa)
  - [Cheatsheet](#cheatsheet)
    - [Fórmula para memorizar](#fórmula-para-memorizar)
  - [Dudas habituales](#dudas-habituales)
    - [¿Por qué hace falta Pillow?](#por-qué-hace-falta-pillow)
    - [¿Por qué usar `ImageField` y no `FileField`?](#por-qué-usar-imagefield-y-no-filefield)
    - [¿Cuándo usar `URLField`?](#cuándo-usar-urlfield)
    - [¿Puedo ofrecer las dos opciones?](#puedo-ofrecer-las-dos-opciones)
    - [¿Por qué usar `null=True` y `blank=True`?](#por-qué-usar-nulltrue-y-blanktrue)
    - [¿Dónde se guardan realmente las imágenes?](#dónde-se-guardan-realmente-las-imágenes)
    - [¿Por qué no funciona solo con `MEDIA_URL`?](#por-qué-no-funciona-solo-con-media_url)
    - [¿Por qué aparece `post.imagen.url`?](#por-qué-aparece-postimagenurl)
    - [¿Por qué usar `{% if post.imagen %}`?](#por-qué-usar--if-postimagen-)
    - [¿Hay que registrar `Post` otra vez en `admin.py`?](#hay-que-registrar-post-otra-vez-en-adminpy)
    - [¿Hay que crear una vista nueva?](#hay-que-crear-una-vista-nueva)
    - [¿Por qué no se ve la imagen en el navegador?](#por-qué-no-se-ve-la-imagen-en-el-navegador)
    - [¿Qué ocurre si cambio el nombre o la carpeta de la imagen?](#qué-ocurre-si-cambio-el-nombre-o-la-carpeta-de-la-imagen)
    - [¿Qué ocurre en producción?](#qué-ocurre-en-producción)
    - [¿Debo subir la carpeta `media/` a Git?](#debo-subir-la-carpeta-media-a-git)

## Objetivo

Permitir que cada post:

1. Tenga una imagen opcional subida al servidor o una URL externa.
2. Se pueda editar desde el panel de administración.
3. Guarde las imágenes subidas en la carpeta `media/`.
4. Muestre cualquiera de las dos opciones en las plantillas.

## 1. Activar el entorno virtual

Desde la raíz del proyecto:

En Windows:

```powershell
.\.env\Scripts\Activate.ps1
```

Si PowerShell bloquea la ejecución de scripts, se puede usar el intérprete directamente:

```powershell
.\.env\Scripts\python.exe --version
```

En Linux o Mac:

```bash
source .env/bin/activate
```

## 2. Instalar Pillow (solo para subir archivos)

`ImageField` necesita la librería Pillow para procesar imágenes.

Pillow solo es necesario si se utiliza la opción de subir la imagen al servidor. Para usar exclusivamente una URL externa, basta con `URLField`.

```powershell
pip install Pillow
```

En [`requirements.txt`](requirements.txt) debe aparecer:

```text
Django
Pillow
```

También se puede actualizar el archivo con:

```powershell
pip freeze > requirements.txt
```

## 3. Elegir cómo guardar la imagen

Hay dos opciones:

- **Opción A: subir la imagen al servidor** con `ImageField`.
- **Opción B: guardar la dirección de una imagen externa** con `URLField`.

También se pueden añadir los dos campos para que cada post permita elegir una opción desde el admin. En ese caso, se recomienda rellenar solo uno de ellos.

### Opción A: subir la imagen al servidor

En [`blog/models.py`](blog/models.py), dentro de la clase `Post`:

```python
imagen = models.ImageField(
    upload_to='posts/',
    null=True,
    blank=True,
)
```

Ejemplo de ubicación dentro del modelo:

```python
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="posts",
        null=True,
        blank=True,
    )
    imagen = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
    )
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField()
```

### Opción B: introducir una URL

Si no se quiere guardar el archivo en el proyecto, añadir en `Post`:

```python
imagen_url = models.URLField(
    max_length=500,
    null=True,
    blank=True,
)
```

Ejemplo usando las dos opciones:

```python
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    # ... relaciones y resto de campos ...
    imagen = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
    )
    imagen_url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
    )
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField()
```

No es obligatorio usar los dos campos. Si se elige solo la opción de URL, se puede omitir `imagen`, Pillow y la configuración `MEDIA_*`.

### Significado de las opciones

- `upload_to='posts/'`: guarda los archivos dentro de `media/posts/`.
- `null=True`: permite que la columna de la base de datos no tenga imagen.
- `blank=True`: permite dejar el campo vacío en formularios y en el admin.

`null=True` y `blank=True` son importantes porque ya existen posts creados antes de añadir este campo.

Si se usan las dos opciones, la plantilla puede dar prioridad a la imagen subida y usar la URL como alternativa.

## 4. Crear y aplicar la migración

Desde la carpeta que contiene `manage.py`:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Se generará una nueva migración en [`blog/migrations/`](blog/migrations/).

## 5. Configurar los archivos multimedia (solo para la opción A)

En [`primerproyecto/settings.py`](primerproyecto/settings.py), debajo de `STATIC_URL`:

```python
STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Diferencia entre ambos ajustes

- `MEDIA_ROOT`: carpeta física del ordenador donde se guardan las imágenes.
- `MEDIA_URL`: prefijo de URL que permite acceder a ellas desde el navegador.

Con esta configuración, una imagen guardada como `posts/foto.jpg` se encontrará físicamente en:

```text
media/posts/foto.jpg
```

Y se podrá solicitar mediante:

```text
/media/posts/foto.jpg
```

## 6. Hacer públicas las imágenes durante el desarrollo (solo para la opción A)

En [`primerproyecto/urls.py`](primerproyecto/urls.py), añade estos imports:

```python
from django.conf import settings
from django.conf.urls.static import static
```

El archivo debe quedar con una configuración equivalente a esta:

```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
```

Esto hace que Django sirva los archivos de `media/` cuando `DEBUG = True`.

> Esta solución es para desarrollo. En producción, normalmente las imágenes las sirve un servidor web o un servicio de almacenamiento.

## 7. Mostrar la imagen en una plantilla

### Plantilla para la opción A: imagen subida

En [`blog/templates/blog/detalle_post.html`](blog/templates/blog/detalle_post.html), dentro del contenido del post:

```html
{% if post.imagen %}
    <img src="{{ post.imagen.url }}"
         alt="{{ post.titulo }}"
         width="300">
{% endif %}
```

El `if` es necesario para que los posts sin imagen sigan funcionando.

También se puede mostrar en [`blog/templates/blog/principal.html`](blog/templates/blog/principal.html):

```html
{% if post.imagen %}
    <img src="{{ post.imagen.url }}"
         alt="{{ post.titulo }}"
         width="150">
{% endif %}
```

### Plantilla para las dos opciones

Para permitir imagen subida o URL externa, usar una condición como esta:

```html
{% if post.imagen %}
    <img src="{{ post.imagen.url }}"
         alt="{{ post.titulo }}"
         width="300">
{% elif post.imagen_url %}
    <img src="{{ post.imagen_url }}"
         alt="{{ post.titulo }}"
         width="300">
{% endif %}
```

Si se elige solo la opción B, la plantilla queda más sencilla:

```html
{% if post.imagen_url %}
    <img src="{{ post.imagen_url }}"
         alt="{{ post.titulo }}"
         width="300">
{% endif %}
```

## 8. Subir una imagen o introducir una URL desde el admin

1. Arrancar el servidor:

   ```powershell
   python manage.py runserver
   ```

2. Abrir `http://127.0.0.1:8000/admin/`.
3. Entrar en `Posts`.
4. Crear o editar un post.
5. Elegir una de estas opciones:
   - Seleccionar una imagen en el campo `Imagen`.
   - Pegar una dirección en el campo `Imagen URL`.
6. Si se usan los dos campos, dejar uno vacío.
7. Guardar.
8. Si se subió un archivo, comprobar que existe `media/posts/`.
9. Abrir el listado o el detalle del post.

## 9. Comprobación completa

El flujo esperado es:

```text
ImageField o URLField en Post
    ↓
makemigrations + migrate
    ↓
Imagen subida o URL introducida desde /admin/
    ↓
Imagen visible con <img>

Si se sube un archivo:

```text
Pillow → MEDIA_ROOT y MEDIA_URL → URL multimedia pública
```

## Cheatsheet

```text
1. Opción A, subir archivo:
   pip install Pillow
   Añadir Pillow a requirements.txt

   blog/models.py:
   imagen = models.ImageField(
       upload_to='posts/',
       null=True,
       blank=True
   )

2. Opción B, usar URL:
   imagen_url = models.URLField(
       max_length=500,
       null=True,
       blank=True
   )

3. Migrar:
   python manage.py makemigrations
   python manage.py migrate

4. Solo para archivos subidos,
   primerproyecto/settings.py:
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'

5. Solo para archivos subidos,
   primerproyecto/urls.py:
   from django.conf import settings
   from django.conf.urls.static import static

   urlpatterns += static(
       settings.MEDIA_URL,
       document_root=settings.MEDIA_ROOT
   )

6. Plantilla con las dos opciones:
   {% if post.imagen %}
       <img src="{{ post.imagen.url }}"
            alt="{{ post.titulo }}">
   {% elif post.imagen_url %}
       <img src="{{ post.imagen_url }}"
            alt="{{ post.titulo }}">
   {% endif %}

7. Probar:
   /admin/ → editar Post
   → seleccionar imagen o pegar URL
   → comprobar el listado/detalle
```

### Fórmula para memorizar

> **Elegir archivo o URL → campo del modelo → migraciones → plantilla `<img>`**

Para archivos subidos:

> **Pillow → ImageField → MEDIA_ROOT → MEDIA_URL**

## Dudas habituales

### ¿Por qué hace falta Pillow?

`ImageField` utiliza Pillow para reconocer y procesar archivos de imagen. Sin Pillow, Django puede mostrar un error indicando que la librería no está instalada.

Si se utiliza únicamente `URLField`, Pillow no es necesario.

### ¿Por qué usar `ImageField` y no `FileField`?

`ImageField` valida que el archivo sea una imagen. `FileField` acepta cualquier tipo de archivo.

### ¿Cuándo usar `URLField`?

Usa `URLField` cuando la imagen ya está alojada en otra web o servicio y solo quieres guardar su dirección. No ocupa espacio en `media/`, pero depende de que la URL siga existiendo y sea accesible.

La URL debe ser directa a una imagen, normalmente comenzar por `https://` y permitir que otros sitios la carguen.

### ¿Puedo ofrecer las dos opciones?

Sí. Añade `imagen` e `imagen_url` al modelo, ejecuta las migraciones y muestra primero `post.imagen` y, con `{% elif %}`, `post.imagen_url`.

Es mejor rellenar solo un campo. Si ambos tienen valor, la plantilla de esta guía muestra primero la imagen subida.

### ¿Por qué usar `null=True` y `blank=True`?

Porque ya hay posts en la base de datos y no todos tienen imagen. Así la imagen es opcional.

- `null=True` afecta a la base de datos.
- `blank=True` afecta a formularios y al panel admin.

### ¿Dónde se guardan realmente las imágenes?

Con `upload_to='posts/'` y `MEDIA_ROOT = BASE_DIR / 'media'`, se guardan en:

```text
media/posts/
```

La imagen no se guarda dentro de `db.sqlite3`; la base de datos guarda su ruta.

Una imagen externa tampoco se guarda en `db.sqlite3`; solo se guarda el texto de su URL.

### ¿Por qué no funciona solo con `MEDIA_URL`?

`MEDIA_URL` solo define el prefijo de la dirección web. Durante el desarrollo también hay que añadir `static(...)` en `primerproyecto/urls.py` para que Django sirva los archivos.

Esto solo afecta a las imágenes subidas. Las imágenes externas se cargan directamente desde su URL.

### ¿Por qué aparece `post.imagen.url`?

El campo de imagen proporciona la URL del archivo mediante `.url`. No se debe escribir manualmente `/media/...` en la plantilla.

### ¿Por qué usar `{% if post.imagen %}`?

Si el post no tiene imagen, acceder directamente a `post.imagen.url` puede producir un error. El `if` evita intentar generar una URL inexistente.

### ¿Hay que registrar `Post` otra vez en `admin.py`?

No. El modelo `Post` ya está registrado. Al añadirle un campo, el campo aparecerá automáticamente en el formulario del admin.

### ¿Hay que crear una vista nueva?

No necesariamente. La imagen pertenece al `Post` y se puede mostrar usando el `post` que ya reciben las vistas de listado y detalle.

### ¿Por qué no se ve la imagen en el navegador?

Comprobar, en este orden:

1. Si se sube archivo, Pillow está instalado en el entorno correcto.
2. Se ejecutaron `makemigrations` y `migrate`.
3. Si se sube archivo, la imagen aparece dentro de `media/posts/`.
4. Si se sube archivo, `MEDIA_URL` y `MEDIA_ROOT` están escritos correctamente.
5. Si se sube archivo, `urls.py` contiene `static(...)`.
6. Si se sube archivo, `DEBUG = True`.
7. La plantilla contiene la condición y el campo elegido.
8. En una URL externa, la dirección empieza por `http://` o `https://` y sigue disponible.
9. El servidor se reinició después de cambiar la configuración.

### ¿Qué ocurre si cambio el nombre o la carpeta de la imagen?

El archivo antiguo no siempre se elimina automáticamente. Hay que revisar manualmente la carpeta `media/` si se hacen pruebas con muchos archivos.

### ¿Qué ocurre en producción?

La configuración con `static(...)` está pensada para desarrollo. En producción se debe configurar un servidor web o un almacenamiento especializado para servir los archivos multimedia.

### ¿Debo subir la carpeta `media/` a Git?

Normalmente no se suben las imágenes de usuario al repositorio. Se puede añadir `media/` al `.gitignore`, salvo que el profesor pida expresamente incluir alguna imagen de prueba.
