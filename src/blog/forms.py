# coding: utf-8
from django import forms


# from .models import Blog


class SearchForm(forms.Form):
    search = forms.CharField(required=False)
    blogOnPage = forms.ChoiceField(required=False, choices=(('10', '10',), ('20', '20',),))

class LikeForm(forms.Form):
    blog_id = forms.CharField(required=True)
