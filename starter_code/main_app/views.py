
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from .models import Category

# Create your views here.

def index(request):
    category = Category.objects.all()
    print(category)
    return render(request, 'home.html', {'categories':  category})




# Create your views here.

def signup(request):
    form=UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request,user)
            return redirect('/')
    return render(request,'signup.html',{'form':form})



