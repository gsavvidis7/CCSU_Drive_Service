from django.shortcuts import render, redirect
from .models import Event, Driver, Rider
from django.contrib.auth.models import User
from django.http import HttpResponse


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

            validentry = Driver.objects.filter(event=eventinstance, driver=userinstance).first()
            if validentry is not None:
                return HttpResponse("Error: You are already signed up to drive for that event.")

            testid = Rider.objects.filter(rider=userinstance, event=eventinstance).first()
            if testid is not None:
                return HttpResponse("Error: You cannot ride and drive for the same event.")

            driverentry = Driver(event=eventinstance, driver=userinstance, capacity=cap)
            driverentry.save()
            return HttpResponse("You have signed up to be a driver.")
        elif type in "rider":
            getriderevent = request.POST.get('eventname')
            ridereventinstance = Event.objects.get(id=getriderevent)
            finddriver = Driver.objects.filter(event=ridereventinstance, capacity__gt=0).first()
            if finddriver is not None:
                getrideruser = request.POST.get('driverid')

                rideruserinstance = User.objects.get(id=getrideruser)

                validrider = Rider.objects.filter(rider=rideruserinstance, event=ridereventinstance).first()
                if validrider is not None:
                    return HttpResponse("Error: You are already signed up to ride for that event.")

                driverinstance = finddriver
                getrider = request.POST.get('driverid')
                riderinstance = User.objects.get(id=getrider)
                riderentry = Rider(driver=driverinstance, rider=riderinstance, event=ridereventinstance)

                testid = Driver.objects.filter(event=ridereventinstance, driver=rideruserinstance).first()
                if testid is not None:
                    return HttpResponse("Error: You cannot ride and drive for the same event.")

                riderentry.save()
                drivercap = finddriver.capacity
                finddriver.capacity = drivercap - 1
                finddriver.save()
                return HttpResponse("You have signed up to be a rider.")
            else:
                return HttpResponse("Sorry: There are no current drivers for this event.")
    else:
        return HttpResponse("Error: Method not POST")


def view_profile(request):
    return render(request, 'events/profile.html')


def view_driver_profile(request):
    getuser = request.user
    drivers = Driver.objects.filter(driver=getuser)
    return render(request, 'events/driverprofile.html', {'drivers': drivers})


def view_rider_profile(request):
    getuser = request.user
    riders = Rider.objects.filter(rider=getuser)
    return render(request, 'events/riderprofile.html', {'riders': riders})


def remove_driver_entry(request):
    if request.method == 'POST':
        getentry = request.POST.get('eventname')
        getperson = request.user
        entry = Driver.objects.get(event=getentry, driver=getperson)
        entry.delete()
        return redirect('view_driver_profile')
    else:
        return redirect('view_driver_profile')


def remove_rider_entry(request):
    if request.method == 'POST':
        getrideruser = request.POST.get('riderid')
        geteventid = request.POST.get('eventid')

        eventinstance = Event.objects.get(id=geteventid)
        userinstance = User.objects.filter(id=getrideruser).first()
        riderentry = Rider.objects.get(rider=userinstance, event=eventinstance)

        getdriveruser = request.POST.get('driverid')
        eventinstance = Event.objects.get(id=geteventid)
        driveruserinstance = User.objects.get(id=getdriveruser)
        driverentry = Driver.objects.filter(event=eventinstance, driver=driveruserinstance).first()

        dcap = driverentry.capacity
        driverentry.capacity = dcap + 1
        driverentry.save()
        riderentry.delete()

        return redirect('view_rider_profile')
    else:
        return redirect('view_rider_profile')
