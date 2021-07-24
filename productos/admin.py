from Usuarios.models import Usuario
from django.contrib import admin
from productos.models import Categoria, Producto, Subcategoria
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
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

class UsuarioAdmin(UserAdmin):
    UserAdmin.fieldsets = (
        (None,{'fields':('username', 'password')}),
        ('Información del Usuario', {'fields':('email','img')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username','email','foto')
    def foto(self, obj):
        print(obj.img.url)
        return format_html("<a href={}><img src={} width='40' height='40'/></a>",obj.img.url,obj.img.url) 


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Usuario,UsuarioAdmin)
