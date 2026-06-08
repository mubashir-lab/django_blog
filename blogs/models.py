from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name= models.CharField(max_length=20,unique=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural= "categories"
    def __str__(self):
        return self.category_name
STATUS_CHOICES=(
    ('Draft','Draft'),
    ('Published','Published')
)
class Blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200,unique=True,blank=True)
    category=models.ForeignKey(Category ,on_delete=models.CASCADE)#jb category delete ho to ussa mila sara blog bhi delete ho gy ga
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='uploads/%y/%m/%d')
    short_description=models.TextField(max_length=300)
    blog_body=models.TextField(max_length=500)
    status=models.CharField( max_length=20,choices=STATUS_CHOICES,default='Draft')
    is_featured=models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
