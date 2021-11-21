from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from apps.users.api.serializers import UserSerializer

User = get_user_model()


class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializers = UserSerializer(users, many=True)
        return Response(users_serializers.data)
