from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    date_time = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length=50, default='NULL')
    content = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    content = models.TextField('')
    date_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)


    def __unicode__(self):
        return self.content[:20]

    class Meta:
        ordering = ['-date_time']