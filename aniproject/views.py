from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def homepage(request):
    return render(request,"index.html")

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        conpass1=request.POST.get('confirmpassword')
        my_user = User.objects.create_user(uname, email, pass1)
        my_user.save()
        return redirect('login')
    return render(request,"sign.html")


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password= request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username and password are incorrect")
    return render(request,"login.html")

