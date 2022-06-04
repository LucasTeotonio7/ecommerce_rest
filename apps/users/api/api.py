from django.shortcuts import get_object_or_404

from urllib import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import \
    UserSerializer, UserListSerializer, UpdateUserSerializer


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer
    queryset = None
    model = User

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.filter(
                is_active=True).values('id','name','username','email')

        return self.queryset

    def list(self, request):
        users = self.get_queryset()
        user_serializer = self.list_serializer_class(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuário cadastrado com sucesso!'
            }, status=status.HTTP_201_CREATED)

        return Response({
            'message': 'Não foi possivel realizar o cadastro',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuário atualizado com sucesso!'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Não foi possivel atualizar o cadastro',
            'errors': user_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'Usuário excluído corretamente!'
            })
        return Response({
            'message': 'Não existe este usuário para excluir'
        }, status=status.HTTP_404_NOT_FOUND)