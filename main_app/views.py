from django.shortcuts import render,redirect
from .models import Blogpost,Category,Contact_me
from main_app.forms import SearchForm
from django.core.paginator import Paginator
from .forms import Cs_UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    posts = Blogpost.objects.all().order_by('id')
    featured_post = Blogpost.objects.get(featured=True)
    three_featured_cards = posts[:3]
    rest_posts = posts.exclude(featured=True).order_by("id")[3:]
    latest_news = posts.order_by("-id")[:10] # meant to add most read news on basis of views count "later on"

    context = {
        'posts' : posts,
        'three_featured_cards':three_featured_cards,
        'rest_posts': rest_posts,
        'latest_news':latest_news,
        'featured_post':featured_post,
    }
    return render(request,'AcutePages/homepage.html',context)
@login_required(login_url='login')
def blogpost(request,slug):
    post = Blogpost.objects.get(slug=slug)
    latest_ten_post = Blogpost.objects.all()[:10]
    context = {
        'post':post,
        "latest_ten_post":latest_ten_post,
        }
    return render(request,'AcutePages/blogpost.html',context)
@login_required(login_url='login')
def category(request):
    all_categories = Category.objects.all()
    context = {
        'all_categories':all_categories
    }
    return render(request,'AcutePages/categories.html',context)
@login_required(login_url='login')
def each_cat(request,id):
    cat = Category.objects.get(id=id)
    all_cat_post = cat.CategoryOf.all()  # all post of that category whose cat_id is (as mentioned in the argument)

    # pagination
    pagination = Paginator(all_cat_post, 10)
    page_number = request.GET.get('page')
    page_obj = pagination.get_page(page_number)
    context = {
        'all_cat_post':all_cat_post,
        'cat':cat,
        'page_obj':page_obj
    }
    return render(request,'AcutePages/each_cat_page.html',context)
@login_required(login_url='login')
def bookmark(request):
    context = {
    
    }
    return render(request,'AcutePages/bookmark.html',context)
@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        data = Contact_me(name=name,subject=subject,email=email,msg=msg)
        data.save()
        messages.success(request,'Message sent sucessfully')
        return redirect('contactPage')
    return render(request,'AcutePages/contact.html')

@login_required(login_url='login')
def search(request):
    # form = SearchForm()
    # if request.method == 'GET':
    #     data = request.GET.get(name=)
        

    context = {}
    return render(request,'AcutePages/search.html',context)

def userRegister(request):
    if request.user.is_authenticated:
        return redirect('blog_homepage')
    else:
        form = Cs_UserCreationForm()
        if request.method =='POST':
            try:
                form = Cs_UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Account sucessfully created')
                    return redirect('login')
            except Exception as e:
                print(e)
        context={'form':form}
        return render(request,'AcutePages/register.html',context)

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('blog_homepage')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password =password)
            if user is not None:
                login(request,user)
                return redirect('blog_homepage')
            else:
                messages.info(request,'Username or password is incorrect')
        context={}
        return render(request,'AcutePages/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')