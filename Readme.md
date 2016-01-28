# README #

Es necesaria al menos la versión **3.4** de **python** (https://www.python.org/downloads/)
La última versión de **pip** (https://pip.pypa.io/en/latest/installing.html#install-pip)

Es recomendable crear un virtualenv donde instalar todas las dependencias del proyecto.
Para instalar la versión de **django** y las dependencias del proyecto haremos **pip install -r requirements/local.txt** 

Creación de la base de datos:
Se encuentra en sqlite por el momento, es el fichero **db.sqlite3**.
En django 1.9 tenemos que hacer uso de las migraciones: https://docs.djangoproject.com/en/1.9/topics/migrations/#workflow
De modo que cuando se efectuen cambios en los modelos haremos **python manage.py makemigrations**, una vez comprobados
los ficheros generados por la migración, ejecutaremos la misma **python manage.py migrate**

Para cargar los estáticos se ejecuta el comando **python manage.py collectstatic**

Una vez sincronizada la base de datos, la ejecución de la aplicación se realiza mediante el comando: **python manage.py runserver**
En linea de comandos se mostrará si la aplicación funciona correctamente y en que ruta podemos acceder.
La ruta por defecto para el administrador es **http://127.0.0.1:8000/admin**


## Requisitos/Dependencias del proyecto (ver requirements/base.txt)

 * django framework
 * Ipdb - debugging (https://github.com/gotcha/ipdb)
 
### Otras posibles dependencias, no requeridas en este momento.
 
 * Djangojs - integración de javascript (http://djangojs.readthedocs.org/en/latest/)
 * Django social - login en fb (http://django-social-auth.readthedocs.org/en/latest/)
 * Django rest framework - crear funcionalidades REST (http://www.django-rest-framework.org/) 
 * Django-dynamic-fixture - creación de datos de prueba (http://django-dynamic-fixture.readthedocs.org/en/latest/index.html)
 * Django-Suit - personalización del panel de administración (http://django-suit.readthedocs.org/en/develop/)
 * Django-Grappelli - personalización del panel de administración (http://grappelliproject.com/)
 * Django Facebook - publicación en fb (http://django-facebook.readthedocs.org/)
 * Pillow - procesamiento de imágenes y dependencia de django facebook (http://pillow.readthedocs.org/)
