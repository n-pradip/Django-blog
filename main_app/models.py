import random
import string
from django.db import models
from tinymce.models import HTMLField

def random_generator():
    gen_data = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(10))
    return gen_data

def slug_generator():
    code = random_generator()
    if Category.objects.filter(slug = code).exists():
        new_code = slug_generator()
        return new_code
    return code

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    slug = models.SlugField(max_length=100 ,null=True)
    image = models.ImageField(upload_to="category_img/")

    # overriding save function for self updating slug iff slug not provided manually
    def save(self,*args,**kwargs):
        if self.slug is None:
            self.slug = slug_generator()
        super(Category, self).save(*args,**kwargs)

    def __str__(self):
        return self.name

# blogpost
class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField()
    slug = models.SlugField(null=True,blank=True)
    date = models.DateTimeField()
    image = models.ImageField(upload_to="blogposts_img/")
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="CategoryOf")
    featured = models.BooleanField(default=False)

    # overriding save function for self updating slug iff slug not provided manually
    def save(self,*args,**kwargs):
        if self.slug is None:
            self.slug = slug_generator()
        super(Blogpost, self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title

class Contact_me(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,null=False,blank=False)
    msg = models.TextField(max_length=2000,null=True,blank=True)

    def __str__(self):
        return self.subject
