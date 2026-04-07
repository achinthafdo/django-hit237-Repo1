from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField('published date', null=True, blank=True)

    def __str__(self):
        return self.title

