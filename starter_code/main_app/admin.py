from django.contrib import admin
from .models import Category
from .models import Topic
from .models import Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Post)
