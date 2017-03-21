from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    CreateAPIView,
)

from django.contrib.auth.models import User
from .serializers import UserSerializer



class ProjectsCreateView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
