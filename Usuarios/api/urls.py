from django.urls import path
from Usuarios.api.api import usuario_api_view,usuario_detail_api_view, Login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('usuarios/usuario/',usuario_api_view, name = 'usuario_api'),
    path('usuarios/usuario/<int:pk>/',usuario_detail_api_view, name = 'usuario_detail_api_view'),
    path('usuarios/login/',Login.as_view(), name = 'usuario_login')
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)