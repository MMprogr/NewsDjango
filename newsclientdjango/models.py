from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('auth.User', related_name='news')
    date = models.DateTimeField()

    def __str__(self):
        return 'News with title: {}'.format(self.title)
