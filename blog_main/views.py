from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from assignments.models import About

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