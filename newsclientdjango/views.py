from rest_framework import viewsets
from rest_framework import permissions
from .models import News
from .serializers import NewsSerializer, UserSerializer
from django.contrib.auth.models import User


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = News.objects.all()
    serializer_class = NewsSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = User.objects.all()
    serializer_class = UserSerializer
