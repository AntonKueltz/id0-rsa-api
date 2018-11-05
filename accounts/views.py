from accounts.serializers import UserSerializer

from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView


class CreateUser(CreateAPIView):
    """
    Route: /users/
    Methods:
      POST - Creates a new User object
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
