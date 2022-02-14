from django.contrib import admin
from main_app.models import Category,Blogpost,Contact_me

admin.site.register(Category)

@admin.register(Blogpost)
class Blogpost(admin.ModelAdmin):
    list_display = ['id','title','category','author']

@admin.register(Contact_me)
class Blogpost(admin.ModelAdmin):
    list_display = ['email','name','subject']

