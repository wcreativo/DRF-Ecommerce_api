from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from apps.users.api.serializers import UserSerializer
from rest_framework.decorators import api_view

User = get_user_model()


@api_view(['GET'])
def user_api_view(request):

    if request.method == 'GET':
        users = User.objects.all()
        users_serializers = UserSerializer(users, many=True)
        return Response(users_serializers.data)
