from django import forms
from django.forms import widgets
from django.forms.widgets import Widget
from .models import Post
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'type': 'text'
            })
        }

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']