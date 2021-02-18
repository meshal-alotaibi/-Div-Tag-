from django import forms
from django.forms import fields
from.models import Post , Topic


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
