from django.db import models
# import user model
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=150)
    
    # method convert object to string

    def __str__(self):
       return self.name

#  1=>m relation between Board and Topic
#  one borde can have many topic 

class Topic(models.Model):
    #  1=>m relation between Board and Topic
    #  one borde can have many topic 
    subject= models.CharField(max_length=150)
    content_text = models.TextField(max_length=3500)
    #  on_delete=> when user delet topic it will deleted from borde also
    category = models.ForeignKey(Category,related_name='topics',on_delete=models.CASCADE)
    created_by= models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    #  to add time auto use DateTimeField(auto_now_add=True)
    created_dt = models.DateTimeField(default=timezone.now)
    





    # method convert object to string

    def __str__(self):
       return self.subject



class Post(models.Model):
    message= models.TextField(max_length=200)
    topic= models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)   
    created_by= models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(default=timezone.now)
     
    # method convert object to string

       



