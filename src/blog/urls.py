"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', BlogDetailView.as_view(), name='current_blog'),
    url(r'^(?P<blog_pk>[0-9]+)/', include('post.urls')),
    url(r'^(?P<blog_pk>[0-9]+)/like/$', 'blog.views.likeBlogByAjax'),
    url(r'^$', BlogListView.as_view(), name='blogs'),
    url(r'^create/$', login_required(BlogCreateView.as_view()), name='blog_create'),
    url(r'^me/$', login_required(MyBlogListView.as_view()), name='my_blogs'),
    url(r'^me/search/$', login_required('blog.views.getBlogsByAjax')),
    url(r'^search/$', 'blog.views.getBlogsByAjax'),
]
