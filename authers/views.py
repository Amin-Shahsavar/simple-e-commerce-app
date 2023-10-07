from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authers.serializers import AutherSerializer
from authers.models import Auther


@api_view(['GET', 'POST'])
def auther_list(request):
    if request.method == 'GET':
        queryset = Auther.objects.all()
        serializer = AutherSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def auther_detail(request, id):
    auther = get_object_or_404(Auther, pk=id)
    if request.method == 'GET':
        serializer = AutherSerializer(auther)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AutherSerializer(auther, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        auther.delete()
        return Response({'message': 'Successfuly deleted...'}, status=status.HTTP_204_NO_CONTENT)
