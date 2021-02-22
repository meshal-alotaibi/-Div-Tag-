from django import forms
from django.db import models
from django.forms import fields
from.models import Post , Topic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['subject',
                  'content_text'
                  ]
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['message' 
                  ]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']

