from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Blog
from .forms import BlogForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .decorators import custom_login_required

# Create your views here.

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully!")
            return redirect('home')
        else:
            messages.error(request,"Invalid Username or Password")
    else:
        return render(request,'login.html')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    messages.success(request,"Logged out!")
    return redirect('login')


def register_user(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Registered successfully!")
            return redirect('home')
        else:
            messages.error(request,"Invalid form")
    else:
        form=SignupForm()
    return render(request,'register.html',{'form':form})

@custom_login_required
def home(request):
    if request.user.is_authenticated:

        blogs = Blog.objects.all()
        return render(request,'home.html',{"blogs":blogs})
    else:
        messages.error(request,"You need to login first")
        return redirect('login')

@custom_login_required
def add_blog(request):
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()
            messages.success(request,"Blog added successfully!")
            return redirect('home')
        else:
            messages.error(request,'Please fill all the fields correctly!')
            print(form.errors)
    else:
        form=BlogForm()
    return render(request,'add_blog.html',{'form':form})


@custom_login_required
def blog_details(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    return render(request,'blog_details.html',{'blog':blog})


def your_blogs(request):
    user_blogs=Blog.objects.filter(author=request.user)
    return render(request,'your_blogs.html',{'user_blogs':user_blogs})


@custom_login_required
def edit_blog(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,"Blog updated successfully!")
            return redirect('your_blogs')
        else:
            messages.error(request,'Please fill all the fields correctly!')
            print(form.errors)
    else:
        form=BlogForm(instance=blog)
        return render(request,'edit_blog.html',{'form':form})


@custom_login_required
def delete_blog(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    if request.method=="POST":
        blog.delete()
        messages.success(request,"Blog deleted successfully!")
        return redirect('home')
    return render(request,'delete_blog.html',{'blog':blog})
