from django import forms
from blogs.models import Category,Blog

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'



class BlogPostForm(forms.ModelForm):
            
    class Meta:
        model = Blog
        fields = ("title",'category','short_description','blog_body','status','is_featured','featured_image')
        