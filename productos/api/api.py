from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from productos.models import Categoria, Producto, Subcategoria
from productos.api.serializers import ProductoSerializer,ProductoListSerializer, CategoriaListSerializer, CategoriaSerializer, SubcategoriaListSerializer, SubcategoriaSerializer

@api_view(['GET','POST'])
def producto_api_view(request):
    # list
    if request.method == 'GET':
        # queryset
        # .values('producto','precio','descripcion')
        productos = Producto.objects.all().values('id','producto','precio','descripcion','img')
        productos_serializer = ProductoListSerializer(productos,many = True)
        return Response(productos_serializer.data,status = status.HTTP_200_OK)
    
    # create
    elif request.method == 'POST':
        productos_serializer = ProductoSerializer(data = request.data)
        # validation
        if productos_serializer.is_valid():
            productos_serializer.save()         
            return Response({'message':'Producto creado correctamente!'},status = status.HTTP_201_CREATED)
        return Response(productos_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def producto_detail_api_view(request,pk=None):
    # queryset
    producto = Producto.objects.filter(id = pk).first()

    # validation
    if producto:

        # retrieve
        if request.method == 'GET': 
            productos_serializer = ProductoSerializer(producto)
            return Response(productos_serializer.data,status = status.HTTP_200_OK)
        
        # update
        elif request.method == 'PUT':
            productos_serializer = ProductoSerializer(producto,data = request.data)
            if productos_serializer.is_valid():
                try:
                    producto.img.delete(save=True)
                except:
                    pass
                productos_serializer.save()
                return Response(productos_serializer.data,status = status.HTTP_200_OK)
            return Response(productos_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        # delete
        elif request.method == 'DELETE':
            producto.delete()
            return Response({'message':'Producto Eliminado correctamente!'},status = status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado un producto con estos datos'},status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def categoria_api_view(request):
    # list
    if request.method == 'GET':
        # queryset
        categorias = Categoria.objects.all().values('id','categoria','descripcion','img')
        categorias_serializer = CategoriaListSerializer(categorias,many = True)
        return Response(categorias_serializer.data,status = status.HTTP_200_OK)
    
    # create
    elif request.method == 'POST':
        categorias_serializer = CategoriaSerializer(data = request.data)
        # validation
        if categorias_serializer.is_valid():
            categorias_serializer.save()         
            return Response({'message':'Categoría creada correctamente!'},status = status.HTTP_201_CREATED)
        return Response(categorias_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def categoria_detail_api_view(request,pk=None):
    # queryset
    categoria = Categoria.objects.filter(id = pk).first()

    # validation
    if categoria:

        # retrieve
        if request.method == 'GET': 
            categorias_serializer = CategoriaSerializer(categoria)
            return Response(categorias_serializer.data,status = status.HTTP_200_OK)
        
        # update
        elif request.method == 'PUT':
            categorias_serializer = CategoriaSerializer(categoria,data = request.data)
            if categorias_serializer.is_valid():
                try:
                    categoria.img.delete(save=True)
                except:
                    pass
                categorias_serializer.save()
                return Response(categorias_serializer.data,status = status.HTTP_200_OK)
            return Response(categorias_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        # delete
        elif request.method == 'DELETE':
            categoria.delete()
            return Response({'message':'Categoria Eliminada correctamente!'},status = status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado una categoría con estos datos'},status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def subcategoria_api_view(request):
    # list
    if request.method == 'GET':
        # queryset
        subcategorias = Subcategoria.objects.all().values('id','subcategoria','categoria','descripcion','img')
        subcategorias_serializer = SubcategoriaListSerializer(subcategorias,many = True)
        return Response(subcategorias_serializer.data,status = status.HTTP_200_OK)
    
    # create
    elif request.method == 'POST':
        subcategorias_serializer = SubcategoriaSerializer(data = request.data)
        # validation
        if subcategorias_serializer.is_valid():
            subcategorias_serializer.save()         
            return Response({'message':'Subcategoría creada correctamente!'},status = status.HTTP_201_CREATED)
        return Response(subcategorias_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def subcategoria_detail_api_view(request,pk=None):
    # queryset
    subcategoria = Subcategoria.objects.filter(id = pk).first()

    # validation
    if subcategoria:

        # retrieve
        if request.method == 'GET': 
            subcategorias_serializer = SubcategoriaSerializer(subcategoria)
            return Response(subcategorias_serializer.data,status = status.HTTP_200_OK)
        
        # update
        elif request.method == 'PUT':
            subcategorias_serializer = SubcategoriaSerializer(subcategoria,data = request.data)
            if subcategorias_serializer.is_valid():
                try:
                    subcategoria.img.delete(save=True)
                except:
                    pass
                subcategorias_serializer.save()
                return Response(subcategorias_serializer.data,status = status.HTTP_200_OK)
            return Response(subcategorias_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        # delete
        elif request.method == 'DELETE':
            subcategoria.delete()
            return Response({'message':'Subcategoría Eliminada correctamente!'},status = status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado una subcategoría con estos datos'},status = status.HTTP_400_BAD_REQUEST)
