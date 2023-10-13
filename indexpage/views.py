import email
from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.
a=True

def index(request):
    if a:
      
        mainobj=Blog.objects.all()
        mainobj=list(mainobj)
        mainobj.reverse()
        user=useremail
        return render(request,"index.html",{"name":mainobj,"user":user})
    else:
        return redirect("login")

def login_user(request):
    if request.method=="POST":
        global useremail
        useremail=request.POST['username']
        password1=request.POST['password']
        user=authenticate(username=useremail,password=password1)
       
        if user is not None:
            global a
            a=True
            login(request,user)
            
            
            return redirect("mainpage")
        else:
            return redirect("login")

    return render(request,"login.html")

def logout_user(request):
    global a
    a=False
    logout(request)
    return redirect("login")

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        useremail=request.POST['email']
        password1=request.POST['password']
        if User.objects.filter(username=username):
            error="username already taken"
            return render(request,"register.html",{"error":error})
        if User.objects.filter(email=useremail):
            error="email already taken"
            return render(request,"register.html",{"error":error})
        user=User.objects.create_user(username=username,email=useremail,password=password1)
        user.save()

        

        return redirect("login")
    return render(request,"register.html")