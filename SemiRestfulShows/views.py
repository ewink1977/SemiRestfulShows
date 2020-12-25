from django.shortcuts import render, redirect, HttpResponse
from .models import Shows

# def homeroute(request):
#     return redirect(request, '/shows')

def newshow(request):
    if request.method == 'GET':
        context = {
            "pagetitle" : "Add A Show"
        }
        return render(request, 'html/newshow.html', context)
    if request.method == 'POST':
        Shows.objects.create(title=request.POST['showtitle'], network=request.POST['shownet'], release_date=request.POST['showreldate'], description=request.POST['showdesc'])
        return redirect('../shows')

def showlist(request):
    context = {
        "showlist" : Shows.objects.all(),
        "pagetitle" : "All Shows",
    }

    return render(request, 'html/home.html', context)

def display_show(request, showid):
    showdisplay = Shows.objects.get(id=showid)

    context = {
        "showinformation" : Shows.objects.get(id=showid),
        "pagetitle" : showdisplay.title
    }
    return render(request, 'html/display_show.html', context)

def edit_show(request, showid):
    if request.method == 'GET':
        showdisplay = Shows.objects.get(id=showid)

        context = {
            "showinformation" : Shows.objects.get(id=showid),
            "pagetitle" : f"Edit { showdisplay.title }",
        }
        return render(request, 'html/editshow.html', context)

