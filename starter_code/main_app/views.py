from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def signup(request):
    form=UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            auth_login(request,user)
            # return redirect('home')


            

    return render(request,'signup.html',{'form':form})


