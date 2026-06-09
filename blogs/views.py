from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Blog,Category

# Create your views here.
def posts_by_category(request,category_id):
    posts=Blog.objects.filter(status='Published',category=category_id)
    # use try except when want to redirect in cse 
    # try:
    #     category=Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    # use get object 404 if you want to error page
    category=get_object_or_404(Category,pk=category_id)
    context={
        'posts':posts,
        'category':category
    }
    return render(request,'post_by_category.html',context)

