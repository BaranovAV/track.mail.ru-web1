# coding: utf-8
from django.contrib.auth import authenticate, login
from django.shortcuts import render, resolve_url
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def show_page(request):
    return render(request, 'core/about.html')


class CreateUser(FormView):
    form_class = UserCreationForm

    def get_success_url(self):
        return resolve_url('blogs')

    template_name = 'core/register.html'

    def form_valid(self, form):
        form.save()
        user = authenticate(username=self.request.POST.get('username'), password=self.request.POST.get('password1'))
        login(self.request, user)
        return super(CreateUser, self).form_valid(form)
