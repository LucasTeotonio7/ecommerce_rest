from django.core.exceptions import ValidationError
from rest_framework import fields, serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class testUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):
        # custom validation
        if 'developer' in value:
            raise serializers.ValidationError(
                'Error, não pode existir um usuário com esse nome')

        return value

    # custom validation
    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError(
                'esse campo não pode ficar vazio!')

        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('email não pode conter nome')

        return value

    def validate(self, data):
        return data

    def create(self, validated_data):
        return User.objects.create(**validated_data)
