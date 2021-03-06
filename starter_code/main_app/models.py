from django.db import models
# import user model
from django.contrib.auth.models import User
from django.utils import timezone

#---------------------------- Categoty ---------------------------- #

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    description = models.CharField(max_length=150)
    img = models.CharField(max_length=1000)
    
    # method convert object to string

    def __str__(self):
       return self.name

    #get_posts_count return the number of post in all topic in specific category
    def get_posts_count(self):
        return Post.objects.filter(topic__category=self).count()

   #gget_topic_count return the number of topic in specific category
    def get_topic_count(self):
        return Topic.objects.filter(category=self).count()

    #gget_last_topic return the last topic wrote in specific category 
    def get_last_topic(self):
        return Topic.objects.filter(category=self).order_by('-created_dt').first()


#---------------------------- Topic ----------------------------#


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
    views= models.PositiveIntegerField(default=0)
    img = models.CharField(max_length=1000)
    
    # method convert object to string
    def __str__(self):
       return self.subject

#---------------------------- Post ----------------------------#

class Post(models.Model):
    comment= models.TextField(max_length=200)
    topic= models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)   
    created_by= models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_dt = models.DateTimeField(default=timezone.now)
     
    # method convert object to string
    def __str__(self):
        truncted_comment = Truncator(self.comment)
        return truncted_comment.chars(30)
       



