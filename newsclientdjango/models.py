from django.db import models
from django.contrib.auth.models import User


class NewsManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class News(models.Model):
    objects = NewsManager()
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='news')
    date = models.DateTimeField()

    def __str__(self):
        return 'News with title: {}'.format(self.title)

    def natural_key(self):
        return self.title
