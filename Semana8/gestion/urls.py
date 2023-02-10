from django.urls import path
from .views import CategoriaApiView, PlatosApiView, PlatoDestroyApiView, ListarCategoriaApiView, RegistroUsuarioApiView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = {
    path('categorias/', CategoriaApiView.as_view()),
    path('platos/', PlatosApiView.as_view()),
    path('plato/<int:pk>', PlatoDestroyApiView.as_view()),
    path('categoria/<int:pk>', ListarCategoriaApiView.as_view()),
    path('registro/', RegistroUsuarioApiView.as_view()),
    path('login/', TokenObtainPairView.as_view())
}
