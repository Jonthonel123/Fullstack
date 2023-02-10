from rest_framework.generics import ListCreateAPIView, DestroyAPIView, ListAPIView, CreateAPIView
from .models import CategoriaModel, PlatoModel, UsuarioModel
from .serializers import CategoriaSerializer, MostrarPlatoSerializer, CategoriaConPlatosSerializer, CrearPlatoSerializer, RegistroUsuarioSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .permissions import SoloAdministradores


class CategoriaApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, SoloAdministradores]
    # select * from categoria
    queryset = CategoriaModel.objects.all()
    serializer_class = CategoriaSerializer


class PlatosApiView(ListCreateAPIView):
    queryset = PlatoModel.objects.all()
    # serializer_class = MostrarPlatoSerializer

    def get(self, request: Request):
        # select * from platos where disponibilidad = true;
        resultado = PlatoModel.objects.filter(disponibilidad=True).all()
        print(resultado)
        serializador = MostrarPlatoSerializer(instance=resultado, many=True)
        print(serializador.data)
        return Response(data={
            'content': serializador.data
        })

    def post(self, request: Request):
        data = request.data
        serializador = CrearPlatoSerializer(data=data)
        valida = serializador.is_valid()

        # select * from platos where nombre = '..' limit 1
        platoExistente = PlatoModel.objects.filter(
            nombre=data.get('nombre')).first()
        if platoExistente:
            return Response(data={
                'message': 'El plato con el nombre {} ya existe'.format(platoExistente.nombre)
            })

        if valida == False:
            return Response(data={
                'message': 'La informacion es invalida',
                'content': serializador.errors

            })

        nuevo_plato = serializador.save()
        print(nuevo_plato)
        serializar = MostrarPlatoSerializer(instance=nuevo_plato)
        return Response(data={
            'message': 'Plato creado exitosamente',
            'content': serializar.data
        })


class PlatoDestroyApiView(DestroyAPIView):
    # queryset = PlatoModel.objects.all()
    # serializer_class = PlatoSerializer

    def delete(self, request: Request, pk: int):

        print(pk)
        platoEncontrado = PlatoModel.objects.filter(
            id=pk, disponibilidad=True).first()
        if platoEncontrado is None:
            return Response(data={
                'message': 'El plato no existe'
            })
        platoEncontrado.disponibilidad = False
        platoEncontrado.save()
        return Response(data={
            'message': 'Plato eliminado exitosamente'
        })


class ListarCategoriaApiView(ListAPIView):
    def get(self, request: Request, pk: int):
        categoriaEncontrada = CategoriaModel.objects.filter(id=pk).first()
        print(categoriaEncontrada)

        if categoriaEncontrada is None:
            return Response(data={
                'message': 'Categoria no existe'
            })
        # select * from platos where categoria_id= ... and id=10
        print(categoriaEncontrada.platos.filter(id=10).all())

        serializador = CategoriaConPlatosSerializer(
            instance=categoriaEncontrada)

        return Response(data={
            'content': serializador.data
        })


class RegistroUsuarioApiView(CreateAPIView):
    def post(self, request: Request):
        serializador = RegistroUsuarioSerializer(data=request.data)
        validacion = serializador.is_valid()

        if validacion is False:
            return Response(data={
                'message': 'Error al crear el usuario',
                'content': serializador.errors
            }, status=400)
        nuevoUsuario = UsuarioModel(**serializador.validated_data)
        nuevoUsuario.set_password(serializador.validated_data.get('password'))
        nuevoUsuario.save()

        return Response(data={
            'messge': 'Usuario creado exitosamente'
        }, status=201)
