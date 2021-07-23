from django.urls import path
from productos.api.api import producto_api_view,producto_detail_api_view, categoria_api_view, categoria_detail_api_view, subcategoria_api_view, subcategoria_detail_api_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('productos/producto/',producto_api_view, name = 'producto_api'),
    path('productos/producto/<int:pk>/',producto_detail_api_view, name = 'producto_detail_api_view'),
    path('categorias/categoria/',categoria_api_view, name = 'categoria_api'),
    path('categorias/categoria/<int:pk>/',categoria_detail_api_view, name = 'categoria_detail_api_view'),
    path('subcategorias/subcategoria/',subcategoria_api_view, name = 'subcategoria_api'),
    path('subcategorias/subcategoria/<int:pk>/',subcategoria_detail_api_view, name = 'subcategoria_detail_api_view'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)