from django.shortcuts import render, redirect
from .models import Event, Driver, Rider


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
        #event =
        #driver =
        #cap = 3
        if type in "driver":
            #driverentry = Driver(event=event, driver=driver, capacity=cap).save()
            return render(request, 'events/driver.html')
        elif type in "rider":
            return render(request, 'events/rider.html')
    else:
        return redirect('index')
