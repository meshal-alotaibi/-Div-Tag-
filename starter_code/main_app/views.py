import django
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import SESSION_KEY, login as auth_login
from django.shortcuts import render , get_object_or_404
from .models import Category , Topic , Post
from .forms import PostForm, NewTopicForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count
# Create your views here.

def index(request):
    category = Category.objects.all()
    topic = Topic.objects.all()
    print(category)
    return render(request, 'home.html', {'categories': category , 'topics':topic})


def category_topics(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category ,pk=category_id)
    topics = category.topics.order_by('-created_dt').annotate(topicPost=Count('posts'))

    return render(request, 'topics.html', {'categories': categories, 'category': category,'topics':topics})

    return render(request, 'topics.html', {'categories': categories, 'category': category})



@login_required
def topic(request, category_id , topic_id):
    topic = get_object_or_404(Topic, category__pk=category_id, pk=topic_id)
    SESSION_KEY = 'view_topic_{}'.format(topic.pk)
    if not request.session.get(SESSION_KEY,False):
        topic.views +=1
        topic.save()
        request.session[SESSION_KEY]=True
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            return redirect('topic', category_id=topic.category.id, topic_id=topic.pk)
    else:
        form = PostForm()
    return render(request, 'topic.html', {'topic': topic , 'form' : form})

def signup(request):
    form=UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request,user)
            return redirect('/')
    return render(request,'signup.html',{'form':form})


def new_topic(request,category_id):
    category = get_object_or_404(Category,pk=category_id)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        user = User.objects.first()

        topic = Topic.objects.create(
            subject=subject,
            category=category,
            created_by=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
        return redirect('category_topics',category_id=category.pk)
    return render(request,'new_topic.html',{'category':category})




@login_required
def new_topic(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.category = category
            topic.created_by = request.user
            topic.save()

            return redirect('category_topics', category_id=category.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'category': category, 'form': form})


# def topic_Posts(request,category_id,topic_id):
#     topic =get_object_or_404(Topic,category__pk=category_id,pk=topic_id)

#     return render(request,'topic_Posts.html',{'topic':topic})