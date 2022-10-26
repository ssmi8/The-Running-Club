from .models import Comment, Post
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'excerpt', 'featured_image',)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
