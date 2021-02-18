from django import forms
from django.forms import fields
from.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['message' ,
                  'topic',
                  'created_by',
                  'created_dt',
                  ]
