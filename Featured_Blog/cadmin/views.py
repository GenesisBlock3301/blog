from django.shortcuts import render,redirect
from blog.form import PostForm
from django.contrib.auth.decorators import login_required


def post_add(request):

    if request.method == 'POST':

        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_add')
    else:
        form = PostForm()
    return render(request, 'post_add.html',{'form':form})

@login_required(login_url='blog_login')
def change_password(request):
    if request.method == "POST":
        user = request.user
        new_password = request.POST.get('new_password')
        user.set_password(new_password)
        user.save()
        s ="success"
        return render(request, 'cadmin/password_change.html',{'sucess':s})
    return render(request,'cadmin/password_change.html')

