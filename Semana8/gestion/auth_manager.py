from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_superuser(self, correo, nombre, apellido, tipoUsuario, password):
        if not correo:
            raise ValueError("El usuario no proporciono el correo")
        correo_normalizado = self.normalize_email(correo)
        nuevo_usuario = self.model(
            correo=correo_normalizado, nombre=nombre, apellido=apellido, tipoUsuario=tipoUsuario)

        nuevo_usuario.set_password(password)
        nuevo_usuario.is_superuser = True
        nuevo_usuario.is_staff = True
        nuevo_usuario.save()
