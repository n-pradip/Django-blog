from django.urls import path
from main_app import views

urlpatterns = [
    path('',views.index,name="blog_homepage"),
    path('login/',views.userLogin,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.userRegister,name="register"),
    path('blogpost/<slug:slug>',views.blogpost,name="blogpostPage"),
    path('categories',views.category,name="categoryPage"),
    path('category/<int:id>',views.each_cat,name="each_categoryPage"),
    path('bookmarks',views.bookmark,name="bookmarksPage"),
    path('contact',views.contact,name="contactPage"),
    path('search',views.search,name="searchPage"),
]
