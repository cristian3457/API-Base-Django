from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Usuarios.models import Usuario
from Usuarios.api.serializers import UsuarioListSerializer, UsuarioSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
@api_view(['GET','POST'])
def usuario_api_view(request):
    # list
    if request.method == 'GET':
        # queryset
        # .values('producto','precio','descripcion')
        usuarios = Usuario.objects.all().values('id','username','email','img')
        usuarios_serializer = UsuarioListSerializer(usuarios,many = True)
        return Response(usuarios_serializer.data,status = status.HTTP_200_OK)
    
    # create
    elif request.method == 'POST':
        usuarios_serializer = UsuarioSerializer(data = request.data)
        # validation
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()         
            return Response({'message':'Usuario creado correctamente!'},status = status.HTTP_201_CREATED)
        return Response(usuarios_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def usuario_detail_api_view(request,pk=None):
    # queryset
    usuario = Usuario.objects.filter(id = pk).first()
    # usuario.set_password('new_password')

    # validation
    if usuario:

        # retrieve
        if request.method == 'GET': 
            usuarios_serializer = UsuarioSerializer(usuario)
            return Response(usuarios_serializer.data,status = status.HTTP_200_OK)
        
        # update
        elif request.method == 'PUT':
            usuarios_serializer = UsuarioSerializer(usuario,data = request.data)
            if usuarios_serializer.is_valid():
                try:
                    usuario.img.delete(save=True)
                except:
                    pass
                usuarios_serializer.save()
                return Response(usuarios_serializer.data,status = status.HTTP_200_OK)
            return Response(usuarios_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        # delete
        elif request.method == 'DELETE':
            usuario.delete()
            return Response({'message':'Usuario Eliminado correctamente!'},status = status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado un usuario con estos datos'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def usuario_login(request):

    if request.method == 'POST': 
        authentication_classes  = False
        usuario = request.data['usuario']
        password = request.data['password']
        user = authenticate(username=usuario, password=password)
        if user is not None:
            # login(request, user)
            usuarios_serializer = UsuarioSerializer(user)
            usuario = Usuario.objects.get(username=usuario)
            token, _ = Token.objects.get_or_create(user=usuario)
            return Response({"data":usuarios_serializer.data,"response":True,"token":token},status = status.HTTP_200_OK)
        else:
            return Response({"response":False},status = status.HTTP_401_UNAUTHORIZED)
    
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        print('token:',token)