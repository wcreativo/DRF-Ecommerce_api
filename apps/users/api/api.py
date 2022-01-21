from rest_framework.response import Response
from django.contrib.auth import get_user_model
from apps.users.api.serializers import UserSerializer, TestSerializer
from rest_framework.decorators import api_view
from rest_framework import status
User = get_user_model()


@api_view(['GET', 'POST'])
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'email', 'password')
        # Convierte cada instancia a JSON
        users_serializers = UserSerializer(users, many=True)
        # test_serializer = TestSerializer(data={"name": "Carolina", "email": "karitoverum@gmail.com"})
        # if test_serializer.is_valid():
        #     test_serializer.save()
        return Response(users_serializers.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # Validación: En base a los campos del modelo analiza la estructura enviada
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):

    user = User.objects.filter(id=pk).first()

    if user:

        if request.method == 'GET':
            # Convierte la instancia a JSON
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            # Actualiza la data si conincide las llaves de la petición con los atributos de la instancia
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            user.delete()
            return Response({"detail": "El usuario ha sido borrado exitosamente"}, status=status.HTTP_200_OK)
    return Response({'detail': 'Usuario no encontrado'}, status=status.HTTP_400_BAD_REQUEST)
