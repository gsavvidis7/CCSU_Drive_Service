from django.shortcuts import render, redirect
from .models import Event, Driver, Rider
from django.contrib import messages
from django.contrib.auth.models import User


def view_events(request):
    events = Event.objects.all()
    return render(request, 'events/events.html', {'events': events})


def view_concerts(request):
    events = Event.objects.filter(type='concert')
    return render(request, 'events/events.html', {'events': events})


def view_sports(request):
    events = Event.objects.filter(type='sport')
    return render(request, 'events/events.html', {'events': events})


def view_other(request):
    events = Event.objects.filter(type='other')
    return render(request, 'events/events.html', {'events': events})


def signup(request):
    if request.method == 'POST':
        type = request.POST.get("type", None)
        if type in "driver":
            getevent = request.POST.get('eventname')
            getuser = request.POST.get('driverid')
            eventinstance = Event.objects.get(id=getevent)
            userinstance = User.objects.get(id=getuser)
            cap = 3
            driverentry = Driver(event=eventinstance, driver=userinstance, capacity=cap)
            driverentry.save()
            return render(request, 'events/driver.html')
        elif type in "rider":
            return render(request, 'events/rider.html')
    else:
        return redirect('index')
