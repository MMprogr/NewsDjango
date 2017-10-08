from rest_framework import serializers
from .models import News
from django.contrib.auth.models import User


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News


class UserSerializer(serializers.ModelSerializer):
    news = serializers.PrimaryKeyRelatedField(
        many=True, queryset=News.objects.all()
    )

    class Meta:
        model = User
