from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                print("Error: Username already taken")
                messages.info(request, 'Error: Username already taken')
                return redirect('register')
            else:
                User.objects.create_user(firstname=firstname, lastname=lastname, username=username, password=password)
                print("Registration complete")
        else:
            print("Error: Passwords must match")
            messages.info(request, 'Error: Passwords must match')
            return redirect('register')

        return redirect('index')

    else:
        return render(request, 'register.html')

