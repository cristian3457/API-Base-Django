from django.contrib import admin
from productos.models import Categoria, Producto, Subcategoria
from django.utils.html import format_html
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display=("producto","precio","descripcion","foto")
    def foto(self, obj):
        print(obj.img.url)
        return format_html("<a href={}><img src={} width='40' height='40'/></a>",obj.img.url,obj.img.url) 

class CategoriaAdmin(admin.ModelAdmin):
    list_display=("categoria","descripcion","foto")
    def foto(self, obj):
        print(obj.img.url)
        return format_html("<a href={}><img src={} width='40' height='40'/></a>",obj.img.url,obj.img.url) 

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display=("subcategoria","categoria","descripcion","foto")
    def foto(self, obj):
        print(obj.img.url)
        return format_html("<a href={}><img src={} width='40' height='40'/></a>",obj.img.url,obj.img.url) 

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
