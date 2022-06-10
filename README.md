<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br/>
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br/>
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr>
            <td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio / Talleres / Centros de Simulación</td>
        </tr>
        <tr>
            <td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td>
            <td><span style="font-weight:bold;">Código</span>: GUIA-PRLE-001</td>
            <td><span style="font-weight:bold;">Página</span>: 1</td>
        </tr>
    </tbody>
</table>
<span style="font-weight:bold;">INFORME DE LABORATORIO</span><br/>

<table>
    <theader>
        <tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
    </theader>
    <tbody>
        <tr>
            <td>ASIGNATURA:</td>
            <td colspan="5">Progamación Web 2</td>
        </tr>
        <tr>
            <td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Django</td>
        </tr>
        <tr>
            <td>NÚMERO DE PRÁCTICA:</td>
            <td>05</td>
            <td>AÑO LECTIVO:</td>
            <td>2022 A</td>
            <td>NRO. SEMESTRE:</td>
            <td>III</td>
        </tr>
        <tr>
            <td>FECHA DE PRESENTACIÓN:</td>
            <td></td>
            <td>HORA DE PRESENTACIÓN:</td>
            <td colspan="3"></td>
        </tr>
        <tr>
            <td colspan="3">INTEGRANTE(s):
                <ul>
                    <li>Azurin Zuñiga Eberth - eazurin@unsa.edu.pe</li>
                    <li>Cárdenas Martínez Franco - fcardenasm@unsa.edu.pe</li>
                    <li>Carrillo Daza Barbara - bcarrillo@unsa.edu.pe</li>
                    <li>Hancco Condori Bryan - bhanccoco@unsa.edu.pe</li>
                    <li>Velita Aguilar Italo - ivelita@unsa.edu.pe</li>
                </ul>
            </td>
            <td>NOTA:</td>
            <td colspan="2"></td>
        </tr>
        <tr>
            <td colspan="6">DOCENTE(s):
                <ul>
                    <li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
</div>

<!-- Reportes -->
## SOLUCIÓN Y RESULTADOS

---

I. SOLUCIÓN DE EJERCICIOS/PROBLEMAS <br>
* Ver tutorial de CRUD hecho para este laboratorio: https://youtu.be/c3g_yYMBx-8
* Despues de clonar el repositorio, tenemos que instalar todas las dependencias
    * Virtual enviroment: Asignado nombre a venv
        ```sh
        # On linux/On Windows
        python3 -m virtualenv venv
        python -m virtualenv venv
        # or
        vitualenv -p python3 venv
        vitualenv -p python venv
        ```
        ```sh
        ├── README.md
        ├── blog
        ├── manage.py
        ├── mysite
        ├── requirements.txt
        └── venv
        ```
    * Luego activamos el entorno virtual e instalamos django con requirements.tct
        ```sh
        # On linux
        source ./venv/bin/activate
        # On Windows
        .\venv\Scripts\activate
        ```
        ```sh
        pip install -r requirements.txt
        ```
    * NOTA: COMO EN EL GITIGNORE SE INCLUYÓ LA BASE DE DATOS EL BLOG ESTARÁ VACIO Y NO MOSTRARÁ NINGUN POST, necesita registrase para empezar a probar la aplicación.

* Si está viendo para testear debe antes incluir los modelos de models.py en la base de datos (Por defecto dbs.sqlite3) para crear las tablas, una vez eso hecho puede correr la aplicación. Si quiere ver el desarrollo puede saltarse a la siguiente parte.
    ```sh
    # Linux
    python3 manage.py migrate

    # Windows
    python manage.py migrate
    ```
    * Cree y acceda como superusuario activo para poder crear posts y tener acceso a la vista de admin en 'localhost:8000/admin.'
    ```sh
    # Creando superusuario
    python manage.py createsuperuser
    ```
    ```sh
    Username (leave blank to use '******'): ****** 
    Email address: ******@******
    Password: 
    Password (again): 
    This password is entirely numeric.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.
    ```
* Se asigno a cada integrante una parte de la aplicación y teniendo una secuencialidad
    * Bryan
      - Siguiendo los pasos propuestos por la página de DjangoGirls, se creo el proyecto, cambio la configuración y creo la aplicación.
      - Después de estos pasos iniciales se definio el __modelo__ de nuestra aplicación, realizando las modificaciones al archivo models.py del blog.
          ```python
             ...
             from django.utils import timezone
             ...
             class Post(models.Model):
                ...
                def publish(self):
                    self.published_date = timezone.now()
                    self.save()

                def __str__(self):
                    return self.title
          ```
       - Para que Django conozca los cambios realizados, se prepara un archivo de migración que se aplicara a la base de datos.
         ```sh
             python manage.py makemigrations blog
             ...
             python manage.py migrate blog
          ```
       - Continuando con el modelo, para poder agregar, editar y borrar los posts, se editó el archivo admin.py del blog.
         ```python
             from django.contrib import admin
             from .models import Post

             admin.site.register(Post)
          ```
    * Franco
    * Bárbara
    * Eberth
    * Italo
        * Creamos la carpeta templates dentro de blog y colocamos un layout.html que será el principal y que se compartira con las otras plantillas, igualmente se incluyó bootstrap en una etiqueta link
        ```sh
        ├── templates
        └── blog
            ├── layout.html
            ├── partials
            │       └── _navbar.html
            ├── post_detail.html
            ├── post_edit.html
            └── post_list.html
        ```
        ```html
        {% load static %}

        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM        +OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
        <link rel="stylesheet" href="{% static 'css/styles.css' %}">
        </head>

        <title>My blog</title>
        </head>
        <body>

            {% include 'blog/partials/_navbar.html' %}

            <div class="container p-4">
            {% block content %}
            {% endblock  %}
            </div>

        </body>
        </html>
        ```
        * También se tuvo que modificar post_list() para que devolviera los post creados a post_list.html
        ```python
        def post_list(request):
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'blog/post_list.html', {'posts': posts}
        ```
        * Se incluyó tambien una carpeta static donde colocamos los estilos personalizados de nuestro blog
        ```sh
        ├── static
        │   └── css
        │       └── styles.css
        ```
        * Para terminar tambien se creo una carpeta partials dentro de templates donde creamos la barra de navegación como _navbar.html
        ```html
        <nav class="navbar navbar-expand-lg bg-black navbar-dark">
        <div class="container">
            <a class="navbar-brand fw-bold" href="/">MI BLOG</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup"      aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav ms-auto">
                <a class="nav-link active" aria-current="page" href="/">Blogs</a>
                {% if user.is_authenticated %}
                <a class="nav-link active" href="/admin">Admin</a>
                {% endif %}
                {% if user.is_authenticated %}
                  <a class="btn btn-primary" href="{% url 'post_new' %}">Crear Post</a>
                {% endif %}
        
              </div>
            </div>
        </div>
        </nav>
        ```

<!-- No quitar el espacio de este comentario puedes escribir hasta arriba-->
---

II. SOLUCIÓN DEL CUESTIONARIO

* ¿Cuál es un estándar de codificación para Python? Ejemplo: Para PHP en el proyecto Pear [https://pear.php.net/manual/en/standards.php](https://pear.php.net/manual/en/standards.php)
    * Para python tenemos [PEP8](https://legacy.python.org/dev/peps/pep-0008/).
    * Esta definida como una GUIA de estilos de codificacion en python.
    * Los usuarios de python llegaron a una convención para poder usar esta guía, contiene recomendaciones con el objetivo de escribir un codigo más legible. [https://ellibrodepython.com/python-pep8](https://ellibrodepython.com/python-pep8)
    * Tiene una función similar a typescript solo que no tiene una extencion propia y sigue trabajando con la extensión .py.
<br>

* ¿Qué diferencias existen entre EasyInstall, pip, y PyPM?
<!-- Debe haber una linea entre el header y la tabla para que renderize -->
| EasyInstall                         | PIP                                    | PYPM                                                           |
|-------------------------------------|----------------------------------------|----------------------------------------------------------------|
| Es gratuito                         | Es gratuito                            | Es de paga <br>(Necesitas una destribución Especial de python) |
| Es el más antiguo                   | Es el reemplazo directo de EasyInstall | Está a la par con pip                                          |
| Viene por defecto en las setuptools | Debes instalarlo manualmente           | Debes instalarlo manualmente                                   |
<br>

* En un proyecto Django que se debe ignorar para usar git. Vea: [https://github.com/django/django/blob/main/.gitignore.](https://github.com/django/django/blob/main/.gitignore) ¿Qué otros tipos de archivos se deberían agregar a este archivo?
    ```ini
    # Created by https://www.toptal.com/developers/gitignore/api/django
    # Edit at https://www.toptal.com/developers/gitignore?templates=django
    # Source https://www.toptal.com/developers/gitignore/

    ### Django ###
    *.log
    *.pot
    *.pyc
    *~
    __pycache__/
    local_settings.py
    db.sqlite3
    db.sqlite3-journal
    .DS_Store
    media

    # Virtual Enviromenents
    venv/
    ```
    * En la carpeta static está todos los archivos que se quiera compartir de forma pública por lo que generalmente no se incluye, sim embargo dependerá mucho de las necesidades del projecto.
    * media/ solo está asociado con el projecto ya construido por lo que lo mejor es omitirlo
    * Las bases de datos tambien se pueden incluir si queremos armar la aplicación desde cero, si la aplicación llegara a tener la necesidad de mantener los datos pues se debe quitar del gitignore.
    * Las carpetas y archivos de los ejecutables como los .pyc, __pycache __, .log .pot, etc. Se deben omitir ya que son la configuración personal de cada host.
    * Para nuestro projecto se sigue manteniendo la opcion de ignorar el venv ya que esto tiene configuraciones diferentes entre windows y basados en unix. El archivo requirements.txt es necesario por si nuestro projecto necesita tanto los modulos como las dependencias sin hacerlas una por una.
    * La mayoria de estos archivos se contruyen al momento de ejecutar de forma local la aplicación, se deberia incluir siempre una guia de uso para orientar a los usuarios
<br>

* Utilice ```python manage.py shell``` para agregar objetos. ¿Qué archivos se modificaron al agregar más objetos?
   * Estando ya dentro del shell de Django, debemos importar el modelo
    ```sh
        >>> from blog.models import Post
    ```
   * Previamente deberíamos haber creado un post con un titulo cualquiera, por ejemplo "Another Test", se puede verificar con el siguiente comando ```Post.objects.all()```. Que nos devolvera un QuerySet, por ejemplo el siguiente.    
   ```sh
        <QuerySet [<Post: This is a test>, <Post: Another Test>]>
   ```
   * Obtenemos el objeto usuario usado en la creación del post "Another Test".
   ```sh
        >>> aut = Post.objects.get(title="Another Test").author
   ```
   * Ahora si podemos crear un modelo
   ```sh
        >>> Post.objects.create(author=aut, title='Test', text='hello')
   ```
   Finalizado el proceso, el nuevo modelo se habra guardado en la base de datos, pudiendosele realizar las correspondientes operaciones CRUD, podemos confirmar que se ha guardado con ```Post.objects.all()```, donde obtendremos un QuerySet actualizado. El archivo modificado es el de db.sqlite3
   ```sh
        <QuerySet [<Post: This is a test>, <Post: Another Test>, <Post: Test>]]>
   ```
---

III. CONCLUSIONES
* Primero el archivo pyvenv.cfg
    ```ini
    # The host is WSL-UBUNTU-22.04 for Windows 10
    home = /usr
    implementation = CPython
    version_info = 3.10.4.final.0
    virtualenv = 20.14.1
    include-system-site-packages = false
    base-prefix = /usr
    base-exec-prefix = /usr
    base-executable = /usr/bin/python3
    ```
* Primero con respecto a la base de datos, es la primera vez que se aprende a usar sqilite3,  desde antes ya sabemos usar mariadb (Mysql) pero este es una nuevo gestor. Aún así es posible que mejor sea usar una de estas otras base de datos.
<br>
* Toda la construcción de la aplicación es una secuencialidad que ayuda a que mantengamos un orden y evitar confusiones al momento de manejar varios archivos 
<br>
* Por ahora solo hemos creado un modelo basado en una guía, mas adelante probablemente se tenga que crear modelos más personalizados para incluir un registro de usuarios y permitir la eliminacion de registros sin la necesidad de entrar al /admin
<br>
* Solo se vio de forma superficial bootstrap, se tendra que profundizar para facilitar la presonalización de las vistas en las páginas web.
<br>
* Más edelante se puede llenar de más contenido a la carpeta static y tambien se podrá agregar una carpeta para los archivos de media.
---
## RETROALIMENTACIÓN GENERAL

---

### REFERENCIAS Y BIBLIOGRAFÍA

<!-- Enlaces otra forma sin nombres clave, los "-" son solo otra forma de hacer listas-->
- https://www.w3schools.com/python/python_reference.asp
- https://docs.python.org/3/tutorial/
- https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Models
- https://tutorial.djangogirls.org/es/django_models/
- https://pear.php.net/manual/en/standards.php
- https://docs.djangoproject.com/en/4.0/
- https://www.youtube.com/watch?v=M4NIs4BM1dk
- https://pypi.org/
- https://pip.pypa.io/en/latest/user_guide/
- https://packaging.python.org/en/latest/tutorials/installing-packages/
- https://www.toptal.com/developers/gitignore/
- https://getbootstrap.com/
- https://legacy.python.org/dev/peps/pep-0008/
- https://ellibrodepython.com/python-pep8
- https://docs.djangoproject.com/en/4.0/topics/auth/customizing/
