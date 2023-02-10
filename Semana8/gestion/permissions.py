from rest_framework.permissions import BasePermission
from .models import UsuarioModel


class SoloAdministradores(BasePermission):
    message = 'Solamente los administradores pueden realizar esta accion'

    def has_permission(self, request, view):
        print(request.user)
        usuario: UsuarioModel = request.user
        print(request.auth)

        print(usuario.tipoUsuario)
        if usuario.tipoUsuario == 'ADMINISTRADOR':
            return True
        else:
            return False


class SoloMozos(BasePermission):
    message = 'Solo los mozos pueden realizar esta accion'

    def has_permission(self, request, view):
        usuario: UsuarioModel = request.user
        if usuario.tipoUsuario == 'MOZO':
            return True
        else:
            return False


class SoloTrabajador(BasePermission):
    message = 'Solo los mozos y administradores pueden realizar esta accion'

    def has_permission(self, request, view):
        usuario: UsuarioModel = request.user
        if usuario.tipoUsuario == 'MOZO' or usuario.tipoUsuario == 'ADMINISTRADOR':
            return True
        else:
            return False
