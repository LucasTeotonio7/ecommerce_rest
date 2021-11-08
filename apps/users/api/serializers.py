from django.core.exceptions import ValidationError
from rest_framework import fields, serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TestUserSerializer(serializers.Serializer):
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

        return value

    def validate(self, data):
        return data

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
        # print(validated_data)
        # return super().update(instance, validated_data)
