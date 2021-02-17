from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render , get_object_or_404
from .models import Category , Topic,Post
from django.contrib.auth.models import User

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


def topic(request, category_id , topic_id):
    topic = get_object_or_404(Topic, category__pk=category_id, pk=topic_id)
    return render(request, 'topic.html', {'topic':topic})
def signup(request):
    form=UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request,user)
            return redirect('/')
    return render(request,'signup.html',{'form':form})



def new_topic(request,board_id):
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