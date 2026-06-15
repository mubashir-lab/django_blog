from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogPostForm
from django.template.defaultfilters import slugify
# Create your views here.


@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.all().count()
    blogs_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blogs_count':blogs_count,

    }
    return render(request,'dashboard/dashboard.html',context)
def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):
    if request.method=='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm()
    context={
        'form':form,
    }
    return render(request,'dashboard/add_category.html',context)

def edit_category(request,id):
    category=get_object_or_404(Category,id=id)
    if request.method=='POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm(instance=category)
    context={
        'form':form,
        'category':category,
    }
    return render(request,'dashboard/edit_category.html',context)

def delete_category(request,id):
    category=get_object_or_404(Category,id=id)
    category.delete()
    return redirect('categories')

# posts

def posts(request):
    posts=Blog.objects.all()
    context={
        'posts':posts,
    }
    return render(request,'dashboard/posts.html',context)

# def add_post(request):

#     if request.method=='POST':
#         form=BlogPostForm(request.POST,request.FILES)
#         if form.is_valid():
#             post=form.save(commit=False) #temporary save the form
#             post.author= request.user
#             post.save()
#             title = form.cleaned_data['title']
#             # post.slug= slugify(title) + '-' + str(post.id)
#             post.slug=f"{slugify(post.title)}-{post.id}"
#             post.save()
#             return redirect('posts')
#         else:
#             print(form.errors)
#     form=BlogPostForm()
#     context={
#         'form':form,
#     }
#     return render(request,'dashboard/add_post.html',context)

from django.utils.text import slugify

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            title = form.cleaned_data['title']
            post.slug = slugify(title)  # temporary slug first

            post.save()  # now ID is created

            # optional: make unique slug with ID
            post.slug = f"{post.slug}-{post.id}"
            post.save()

            return redirect('posts')
        else:
            print(form.errors)

    form = BlogPostForm()
    return render(request, 'dashboard/add_post.html', {'form': form})


def edit_post(request,id):
    post=get_object_or_404(Blog,id=id)
    if request.method=='POST':
        form=BlogPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
           post= form.save()
           title= form.cleaned_data['title']
           post.slug= slugify(title)+'-'+str(post.id)
           post.save()
           return redirect('posts')

    form=BlogPostForm(instance=post)
    context={
        'form':form,
        'post':post,
    }
    return render(request,'dashboard/edit_post.html',context)


def delete_post(request,id):
    post=get_object_or_404(Blog,id=id)
    post.delete()
    return redirect('posts')