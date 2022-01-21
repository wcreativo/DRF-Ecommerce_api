from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

    def to_representation(self, instance):
        # Modifica el render del listado si no usamos el .values en la vista se usa instance.id
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password'],
        }


class TestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):
        if 'develop' in value:
            raise serializers.ValidationError(
                'No se puede utilizar develop como nombre de usuario')
        return value

    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError('Debes ingresar un correo')
        return value

    def validate(self, data):
        # En data se encuentran todos los campos del modelo

        if data['name'] in data['email']:
            raise serializers.ValidationError('El email no puede contener el nombre')
        return data

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
