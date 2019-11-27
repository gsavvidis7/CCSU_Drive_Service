from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def loginpg(request):
    return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("Error: Username already taken")
                messages.info(request, 'Error: Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("Error: Email already registered")
                messages.info(request, 'Error: Email already registered')
                return redirect('register')
            else:
                User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username,
                                         password=password1)
                print("Registration complete")
        else:
            print("Error: Passwords must match")
            messages.info(request, 'Error: Passwords must match')
            return redirect('register')

        return redirect('index')

    else:
        return render(request, 'register.html')
