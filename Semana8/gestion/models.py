from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .auth_manager import UsuarioManager


class CategoriaModel(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        # sirve para definir los atributos de la clase que estamos heredando
        # directamente para pasarle la metadata sin utilizar el metodo super
        db_table = 'categorias'
        ordering = ['nombre', 'id']


class PlatoModel(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, unique=True, null=False)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(
        auto_now_add=True, db_column='fecha_creacion')

    categoria = models.ForeignKey(
        to=CategoriaModel, on_delete=models.PROTECT, db_column='categoria_id', related_name='platos')

    class Meta:
        db_table = 'platos'


class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(null=False)
    tipoUsuario = models.CharField(max_length=40, choices=[
        ('ADMIN', 'ADMINISTRADOR'),
        ('MOZO', 'MOZO'),
        ('CLIENTE', 'CLIENTE')
    ])
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'tipoUsuario']

    objects = UsuarioManager()

    class Meta:
        db_table = 'usuarios'
