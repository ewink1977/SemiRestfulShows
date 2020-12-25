from django.shortcuts import render, redirect, HttpResponse
from .models import Shows

def homeroute(request):
    return redirect(request, '../shows')

def newshow(request):
    if request.method == 'GET':
        context = {
            "pagetitle" : "Add A Show"
        }
        return render(request, 'html/newshow.html', context)
    if request.method == 'POST':
        pass

def showlist(request):
    context = {
        "showlist" : Shows.objects.all(),
        "pagetitle" : "All Shows"
    }

    return render(request, 'html/home.html', context)

def display_show(request):
    showdisplay = Shows.objects.get(id=request.GET['showid'])

    context = {
        "showinformation" : Shows.objects.get(id=request.GET['showid']),
        "pagetitle" : f"{ showdisplay.name } display!"
    }
    return render(request, 'html/display_show.html', context)



