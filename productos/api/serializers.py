from django.db import models
from rest_framework import serializers

from productos.models import Categoria, Producto, Subcategoria
from drf_extra_fields.fields import Base64ImageField

class ProductoSerializer(serializers.ModelSerializer):
    img  = Base64ImageField(required = False)
    class Meta:
        model = Producto
        fields = '__all__'

    def create(self,validated_data):
        producto = Producto(**validated_data)
        producto.save()
        return producto
    
    def update(self,instance,validated_data):
        updated_producto = super().update(instance,validated_data)
        updated_producto.save()
        return updated_producto


class ProductoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto

    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'producto': instance['producto'],
            'precio': instance['precio'],
            'descripcion': instance['descripcion'],
            'img': instance['img'],
        }


class CategoriaSerializer(serializers.ModelSerializer):
    img  = Base64ImageField(required = False)
    class Meta:
        model = Categoria
        fields = '__all__'

    def create(self,validated_data):
        categoria = Categoria(**validated_data)
        categoria.save()
        return categoria
    
    def update(self,instance,validated_data):
        updated_categoria = super().update(instance,validated_data)
        updated_categoria.save()
        return updated_categoria


class CategoriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria

    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'categoria': instance['categoria'],
            'descripcion': instance['descripcion'],
            'img': instance['img'],
        }

class SubcategoriaSerializer(serializers.ModelSerializer):
    img  = Base64ImageField(required = False)
    class Meta:
        model = Subcategoria
        fields = '__all__'

    def create(self,validated_data):
        subcategoria = Subcategoria(**validated_data)
        subcategoria.save()
        return subcategoria
    
    def update(self,instance,validated_data):
        updated_subcategoria = super().update(instance,validated_data)
        updated_subcategoria.save()
        return updated_subcategoria


class SubcategoriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria

    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'categoria': instance['categoria'],
            'subcategoria': instance['subcategoria'],
            'descripcion': instance['descripcion'],
            'img': instance['img'],
        }