# coding: utf-8
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from pip._vendor.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Blog(models.Model):
    title = models.CharField(max_length=255, default=u'')
    text = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_blogs')
    author = models.ForeignKey(User)
    date = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)

    class Meta:
        verbose_name = u'Блог'
        verbose_name_plural = u'Блоги'
        ordering = ('-title', )

    def __str__(self):
        return self.title
