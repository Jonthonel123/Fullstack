## Crear el Entorno virtual

```
python -m venv entorno_prueba
```

## Activar el entorno virtual

```
source entorno_prueba/Scripts/activate
```

## Instalar django

```
pip install django
pip freeze > requirements.txt
django-admin startproject restaurante .
```

## Correr el servicio

```
cd django_intro
python manage.py runserver
```

## Migrar los modelos

```
python manage.py migrate
```

## Crear un super usuario

```
python manage.py createsuperuser
```

## crear una app

```
python manage.py startapp almacen
```

## Registramos nuestra app en INSTALED_APPS

```
python
INSTALLED_APPS=[
    ....,
    'almacen',
]
```

## Crear nuestro nuevo model y migrar

´´´
python manage.py makemigrations
python manage.py migrate
´´´

## Instalar Django Rest Framework

```
pip install djangorestframework
```

## Agegar DRF a INSTALLED_APPS

```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Documentar nuestra API con Swagger y Redoc

```
pip install drf-yasg
```

## Configuar 'drf-yasg'

settign.py

'drf_yasg',

```
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ...
]
```
