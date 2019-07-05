from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import  Paginator, PageNotAnInteger, EmptyPage
from Featured_Blog import helpers
from .models import *
from django.contrib import messages
from .form import *
from django.core.mail import send_mail
from django.contrib import auth
from cadmin.forms import *


def home(request):
    return render(request,'blog/home.html')

def post_list(request):
    posts = Post.objects.all()
    posts = helpers.pg_records(request, posts,5)
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,id):
    post =get_object_or_404(Post,pk=id)
    context ={'post':post,}
    # try:
    #     post = Post.objects.get(id=id)
    #     context ={"post":post}
    # except:
    #     msg="there is no post"
    #     context = {'msg':msg}
    return render(request,'blog/post_detail.html',context)

def post_by_catagory(request,name):
    post = Catagory.objects.get(name=name)
    posts =post.posts.all()
    return render(request,"blog/post_by_catagory.html",{"posts":posts})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            subject = "You have a new feedback from {}:{}".format(name,sender)
            message = "Subject: {}\n\nMessage: {}".format(form.cleaned_data['subject'], form.cleaned_data['message'])
            print(form.cleaned_data['message'])
            send_mail(subject, message, sender,['mdnuraminsifat380@gmail.com'])
            form.save()
            messages.add_message(request,messages.INFO,'Submitted')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form':form})


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully.")
            return redirect('blog_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form':form})


def login(request):
    if request.user.is_authenticated:
        return redirect('admin_page')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #print(username)
        #print(password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('admin_page')
        else:
            messages.error(request,"Error wrong username/password")
    return render(request, 'blog/login.html')

def logout(request):
    auth.logout(request)
    return render(request,'blog/logout.html')

def admin_page(request):
    if not request.user.is_authenticated:
        return redirect('blog_login')
    return render(request, 'cadmin/admin_page.html')
