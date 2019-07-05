from django.urls import path
from blog.views import *


urlpatterns = [
    path('home/',home,name = 'home'),
    path('',post_list,name="post_list"),
    path("detail/<int:id>/",post_detail, name ='detail'),
    path('catagory/<name>/',post_by_catagory, name = 'catagory'),
    path('contact/',contact, name = 'contact'),
    path('signup/',signup, name = 'signup'),
    path('login/',login, name='blog_login'),
    path('logout/',logout , name = "blog_logout"),
    path('admin_page/',admin_page , name = 'admin_page'),

]