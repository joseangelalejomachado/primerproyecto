# Anotaciones sobre comandos en python para DJango

## MODELOS DJANGO

Estos comandos se aplican en la terminal dentro del entorno virtual de python que hemos creado para nuestro proyecto.

### Creación de modelos

Dentro de una de nuestras aplicaciones tendremos un archivo `models.py` en el que definimos los modelos.

Cada clase corresponde a una tabla, cada atributo de la clase es una columna y cada instancia de la clase es una fila.

Por ejemplo, en el archivo `blog/models.py` podemos definir un modelo `Post` de la siguiente manera:

```python
from django.db import models

# Create your models here.
# Cada clase corresponde a una tabla, cada atributo de la clase es una columna y cada instancia de la clase es una fila
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=60) 
    # En CharField es obligatoria la longitud máxima. Equivale al varchar
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField()
```

### Migraciones

Este modelo se traduce en una tabla de base de datos. Para crear la tabla correspondiente, debemos realizar una migración.

Esta migración se separa en dos pasos: Preparar la migración y aplicarla.

#### Preparar migracion

Para preparar la migración, ejecutamos el siguiente comando:

```bash
python3 manage.py makemigrations
```

- Este comando creará un archivo de migraciones de los modelos que hemos definido y que aún no han sido migrados. Este archivo se encuentra en la carpeta `migrations` de nuestra aplicación.

Si quisieramos preparar la migración de una aplicación concreta, podemos especificarla:

```bash
python3 manage.py makemigrations blog
```

Output en nuestro caso:

```zsh
     ~/g/D/primerproyecto     main !1  python3 manage.py makemigrations     
Migrations for 'blog':
  blog/migrations/0001_initial.py
    + Create model Post
```

#### Aplicar migracion

Para aplicar la migración, ejecutamos el siguiente comando:

```bash
python3 manage.py migrate
```

- La primera vez que ejecutamos este comando, Django aplicará todas las migraciones pendientes de todas las aplicaciones.

Output:

```zsh
     ~/g/D/primerproyecto     main !2 ?2  python3 manage.py migrate     
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

Si queremos especificar la migración sólo de la aplicación `blog`:

```bash
python3 manage.py migrate blog
```

A continuación deberíamos crear un usuario admin:

```bash
python3 manage.py createsuperuser
```

E introducimos los datos que nos solicita. Una vez creado, levantamos el servidor con `python3 manage.py runserver` y podemos acceder al panel de administración de Django en la ruta `/admin` de nuestra aplicación.

Output:

```bash
     ~/g/D/primerproyecto     main !3 ?2  python3 manage.py createsuperuser
Username (leave blank to use 'user'): admin
Email address: 
Password: 
Password (again): 
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
     ~/g/D/primerproyecto     main +5 !2                    ✔  4m 9s    .env    10:36:44   
     ~/g/D/primerproyecto     main +5 !2  python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 28, 2026 - 09:36:51
Django version 6.1.2, using settings 'primerproyecto.settings'
Starting WSGI development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.1/howto/deployment/
Not Found: /
[28/Oct/2026 09:36:54] "GET / HTTP/1.1" 404 2385
[28/Oct/2026 09:36:59] "GET /admin/ HTTP/1.1" 302 0
[28/Oct/2026 09:36:59] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4307
[28/Oct/2026 09:36:59] "GET /static/admin/css/dark_mode.css HTTP/1.1" 200 3583
[28/Oct/2026 09:36:59] "GET /static/admin/css/base.css HTTP/1.1" 200 24538
[28/Oct/2026 09:36:59] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2814
[28/Oct/2026 09:36:59] "GET /static/admin/css/login.css HTTP/1.1" 200 951
[28/Oct/2026 09:36:59] "GET /static/admin/js/theme.js HTTP/1.1" 200 1708
[28/Oct/2026 09:36:59] "GET /static/admin/css/responsive.css HTTP/1.1" 200 15025
[28/Oct/2026 09:36:59] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 3208
[28/Oct/2026 09:37:04] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[28/Oct/2026 09:37:04] "GET /admin/ HTTP/1.1" 200 7155
[28/Oct/2026 09:37:04] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 442
[28/Oct/2026 09:37:04] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 593
[28/Oct/2026 09:37:04] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 978
[28/Oct/2026 09:38:42] "GET /admin/blog/post/ HTTP/1.1" 200 8492
[28/Oct/2026 09:38:42] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6216
[28/Oct/2026 09:38:42] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 11452
[28/Oct/2026 09:38:42] "GET /static/admin/js/core.js HTTP/1.1" 200 6432
[28/Oct/2026 09:38:42] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 349
[28/Oct/2026 09:38:42] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 285314
[28/Oct/2026 09:38:42] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[28/Oct/2026 09:38:42] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1575
[28/Oct/2026 09:38:42] "GET /static/admin/js/actions.js HTTP/1.1" 200 8999
[28/Oct/2026 09:38:42] "GET /static/admin/js/urlify.js HTTP/1.1" 200 9985
[28/Oct/2026 09:38:42] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 325171
[28/Oct/2026 09:38:42] "GET /static/admin/js/filters.js HTTP/1.1" 200 1099
[28/Oct/2026 09:38:42] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 593
[28/Oct/2026 09:38:44] "GET /admin/ HTTP/1.1" 200 7155
```
