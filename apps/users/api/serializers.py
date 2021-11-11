from django.core.exceptions import ValidationError
from rest_framework import fields, serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'nome_usuario': instance['username'],
            'email': instance['email'],
            'senha': instance['password'],
        }
