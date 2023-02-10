from rest_framework import serializers
from .models import CategoriaModel, PlatoModel, UsuarioModel


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'


class MostrarPlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        exclude = ['disponibilidad']
        depth = 1


class CrearPlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatoModel
        exclude = ['disponibilidad']


class CategoriaConPlatosSerializer(serializers.ModelSerializer):
    info_adicional = CrearPlatoSerializer(many=True, source='platos')

    class Meta:
        model = CategoriaModel
        fields = '__all__'
        # depth = 1


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UsuarioModel
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
