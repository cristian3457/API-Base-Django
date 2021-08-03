from django.urls import path
from Usuarios.api.api import ValidaToken, usuario_api_view,usuario_detail_api_view, Login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('usuarios/usuario/',usuario_api_view, name = 'usuario_api'),
    path('usuarios/usuario/<int:pk>/',usuario_detail_api_view, name = 'usuario_detail_api_view'),
    path('usuarios/login/',Login.as_view(), name = 'usuario_login'),
    path('usuarios/validaToken/',ValidaToken.as_view(), name = 'valida_token'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)