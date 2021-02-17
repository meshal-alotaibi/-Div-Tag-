import django
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render , get_object_or_404
from .models import Category , Topic , Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    category = Category.objects.all()
    topic = Topic.objects.all()
    print(category)
    return render(request, 'home.html', {'categories': category , 'topics':topic})


def category_topics(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category ,pk=category_id)
    return render(request, 'topics.html', {'categories': categories, 'category': category})


@login_required
def topic(request, category_id , topic_id):
    topic = get_object_or_404(Topic, category__pk=category_id, pk=topic_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            return redirect('topic', category_id= category.id, topic_id = topic_pk)
    else:
        form = PostForm()
    return render(request, 'topic.html', {'topic': topic , 'form' : form})

# @login_required
# def post(request, category_id, topic_id):
#     topic = get_object_or_404(Topic, category__pk=category_id, pk=topic_id)
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.topic = topic
#             post.created_by = request.user
#             post.save() 
#             return render('topic', category_id=category_id, topic_pk= topic_id)
#     else:
#         form = PostForm()

#     return render(request, 'topic.html', {'topic': topic})


def signup(request):
    form=UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request,user)
            return redirect('/')
    return render(request,'signup.html',{'form':form})



