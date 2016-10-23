from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import resolve_url

# Create your views here.
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from .forms import CommentForm
from .models import *


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'post'


def addCommentToPost(request, pk, blog_pk):
    if request.is_ajax() and request.user.is_authenticated():
        form = CommentForm(request.POST)
        form.is_valid()
        comment = Comment(author=request.user, text=request.POST.get('text'), source_post_id=pk)
        comment.save()
        return HttpResponse(request.POST.get('text'))
    else:
        raise PermissionDenied


class CreatePost(CreateView):
    model = Post
    template_name = 'post/new_post.html'
    context_object_name = 'post'
    fields = ('title', 'text',)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def get_success_url(self):
        return resolve_url('current_post', blog_pk=self.blog.pk, pk=self.object.pk)

    def form_valid(self, form):
        form.instance.source_blog = self.blog
        return super(CreatePost, self).form_valid(form)

    def dispatch(self, request, blog_pk=None, *args, **kwargs):
        self.blog = Post.source_blog.get_queryset().filter(pk=blog_pk)[0]
        return super(CreatePost, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        context['blog'] = self.blog
        return context
