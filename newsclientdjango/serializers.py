from rest_framework import serializers
from .models import News
from django.contrib.auth.models import User


class NewsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = News
        fields = ('title', 'content', 'author', 'date')


class UserSerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=True, required=False )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'news')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
