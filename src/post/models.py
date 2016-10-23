# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Post(models.Model):
    source_blog = models.ForeignKey('blog.Blog', verbose_name='blog')
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
        ordering = ('-title', )

    def __str__(self):
        return self.title


class Comment(models.Model):
    source_post = models.ForeignKey('post.Post', verbose_name='post')
    text = models.TextField()
    author = models.ForeignKey(User)
    date = models.DateTimeField(verbose_name='creation_date', auto_now_add=True)

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'

    def __unicode__(self):
        return self.source_post.text + ' - {} {}'.format(u'Комментарий', self.pk)