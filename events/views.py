from django.shortcuts import render, redirect
from .models import Event, Driver, Rider
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
            getdriver = request.POST.get('driverid')
            eventinstance = Event.objects.get(id=getevent)
            userinstance = User.objects.get(id=getdriver)
            cap = request.POST.get('captext')
            driverentry = Driver(event=eventinstance, driver=userinstance, capacity=cap)
            driverentry.save()
            return render(request, 'events/driver.html')
        elif type in "rider":
            getriderevent = request.POST.get('eventname')
            ridereventinstance = Event.objects.get(id=getriderevent)
            finddriver = Driver.objects.filter(event=ridereventinstance, capacity__gt=0).first()
            if finddriver is not None:
                driverinstance = finddriver
                getrider = request.POST.get('driverid')
                riderinstance = User.objects.get(id=getrider)
                riderentry = Rider(driver=driverinstance, rider=riderinstance)
                riderentry.save()
                test = finddriver.capacity
                finddriver.capacity = test - 1
                finddriver.save()
                return render(request, 'events/rider.html')
            else:
                return render(request, 'events/none.html')
    else:
        return redirect('index')
