from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()

    def validate_name(self, value):
        print("Validate_name")
        if 'develop' in value:
            raise serializers.ValidationError(
                'No se puede utilizar develop como nombre de usuario')

    def validate(self, data):
        # En data se encuentran todos los campos del modelo
        print("Validate")
        return data

    def create(self, validated_data):
        user = User.objects.create()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

    # El serializador primero analiza si hay funciones definidas validate_nombre_del_campo, luego el metodo validate
