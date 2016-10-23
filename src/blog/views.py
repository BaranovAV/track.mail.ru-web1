# coding: utf-8

# Create your views here.
from django.contrib.auth.models import User
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import resolve_url
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import SearchForm, LikeForm
from .models import Blog
from django.conf import settings


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blogs.html'
    context_object_name = 'blogSet'

    def dispatch(self, request, *args, **kwargs):
        self.form = SearchForm(request.GET)
        self.form.is_valid()
        return super(BlogListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return getBlogs(self.form)

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

class MyBlogListView(ListView):
    model = Blog
    template_name = 'blog/my_blogs.html'
    context_object_name = 'blogSet'

    def dispatch(self, request, *args, **kwargs):
        self.request = request;
        self.form = SearchForm(request.GET)
        self.form.is_valid()
        return super(MyBlogListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return getBlogsForUser(self.form,self.request)

    def get_context_data(self, **kwargs):
        context = super(MyBlogListView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['me_liked'] = context['blog'].likes.filter(id=self.request.user.id).count() == 1
        return context

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/blog_creation.html'
    context_object_name = 'blog'
    fields = ('title','text',)

    def get_success_url(self):
        return resolve_url('my_blogs')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BlogCreateView, self).form_valid(form)


def getBlogsByAjax(request):
    if request.is_ajax():
        form = SearchForm(request.GET)
        form.is_valid()
        result = getBlogs(form)
        result['data'] = serializers.serialize('json', result['data'])
        return JsonResponse(result)
    else:
        raise PermissionDenied


def likeBlogByAjax(request, blog_pk):
    if request.is_ajax() and request.user.is_authenticated():
        blog = Blog.objects.get(pk=blog_pk)
        if (blog.likes.filter(id=request.user.id).count()):
            blog.likes.remove(User.objects.get(id=request.user.id))
        else:
            blog.likes.add(User.objects.get(id=request.user.id))
        result = {'data': blog.likes.count()}
        return JsonResponse(result)
    else:
        raise PermissionDenied

# ------ функция для получения списка блогов


def getBlogs(form):
    blogs = Blog.objects.all()
    result = {'data': blogs, 'count': len(blogs)}
    if form and form.cleaned_data['search'] != '':
        result['data'] = blogs.filter(title__contains=form.cleaned_data['search'])
        result['countFiltered'] = len(result['data'])
    return result

def getBlogsForUser(form, request):
    blogs = Blog.objects.filter(author=request.user.id)
    result = {'data': blogs, 'count': len(blogs)}
    if form and form.cleaned_data['search'] != '':
        result['data'] = blogs.filter(title__contains=form.cleaned_data['search'])
        result['countFiltered'] = len(result['data'])
    return result