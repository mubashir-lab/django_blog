from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from assignments.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    featured_post=Blog.objects.filter(is_featured=True).order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status='Published').order_by('updated_at')
    try:
        about=About.objects.get()
    except:
        about=None
    context={
        'about':about,
        'f_post':featured_post,
        'posts':posts
    }

    return render(request,'home.html',context)

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form =RegistrationForm()
    context={
        'registrationform':form
    }
    return render(request ,'register.html',context)


def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form=AuthenticationForm()
    context={
        'login':form
    }
    return render(request,'login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('home')