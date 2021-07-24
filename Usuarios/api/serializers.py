from django.db import models
from rest_framework import serializers

from Usuarios.models import Usuario
from drf_extra_fields.fields import Base64ImageField

class UsuarioSerializer(serializers.ModelSerializer):
    img  = Base64ImageField(required = False)
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self,validated_data):
        usuario = Usuario(**validated_data)
        usuario.set_password(validated_data['password'])  
        usuario.save()
        return usuario
    
    def update(self,instance,validated_data):
        updated_usuario = super().update(instance,validated_data)
        updated_usuario.set_password(validated_data['password'])
        updated_usuario.is_active = True
        updated_usuario.save()
        return updated_usuario


class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario

    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'img': instance['img'],
        }
