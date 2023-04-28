from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, request
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,'home.html')


def loginfun(request):
    return render(request,'login.html')


def readlogin(request):
    unmae = request.POST['tbusername']
    password = request.POST['tbpass']
    user = authenticate(username=unmae, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return redirect('displaystudent')
    else:
        return render(request, 'login.html')


def registerfun(request):
    return render(request,'register.html')


def register_read(request):
    username = request.POST['tbusername']
    password = request.POST['tbpass']
    email = request.POST['tbemail']
    user = User.objects.create_superuser(username=username, email=email, password=password)
    user.save()
    return render(request, 'login.html', {'name':username,'msg': f'user created successfully username is {username}'})


def logoutfun(request):
    logout(request)
    return redirect('login')