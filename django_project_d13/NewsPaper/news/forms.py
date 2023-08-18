from django import forms
from .models import Post


class PostFormNW(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'rating', 'categories', 'postAuthor']


class PostFormAR(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'rating', 'categories', 'postAuthor']
