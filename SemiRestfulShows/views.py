from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Shows

def newshow(request):
    if request.method == 'GET':
        context = {
            "pagetitle" : "Add A Show"
        }
        return render(request, 'html/newshow.html', context)
    if request.method == 'POST':
        errors = Shows.objects.basicvalidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='danger')
            return redirect('newshow')
        else:
            Shows.objects.create(title=request.POST['showtitle'], network=request.POST['shownet'], release_date=request.POST['showreldate'], description=request.POST['showdesc'])
            messages.success(request, f"{ request.POST['showtitle'] } created successfully!")
            return redirect('showlist')

def showlist(request):
    context = {
        "showlist" : Shows.objects.all(),
        "pagetitle" : "All Shows",
    }

    return render(request, 'html/home.html', context)

def display_show(request, showid):
    showdisplay = Shows.objects.get(id=showid)

    context = {
        "showinformation" : showdisplay,
        "pagetitle" : showdisplay.title
    }
    return render(request, 'html/display_show.html', context)

def editshow(request, showid):
    if request.method == 'GET':
        showdisplay = Shows.objects.get(id=showid)

        context = {
            "showinformation" : showdisplay,
            "pagetitle" : f"Edit { showdisplay.title }",
        }
        return render(request, 'html/editshow.html', context)

def updateshow(request, showid):
    if request.method == 'POST':
        update = Shows.objects.get(id=showid)
        errors = Shows.objects.basicvalidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='danger')
            return redirect('display_show', update.id)    
        if request.POST['showtitle']:
            update.title = request.POST['showtitle']
        if request.POST['shownet']:
            update.network = request.POST['shownet']
        if request.POST['showreldate']:
            update.release_date = request.POST['showreldate']
        if request.POST['showdesc']:
            update.description = request.POST['showdesc']
        update.save()
        messages.success(request, f"{ update.title } edited successfully!")
        return redirect('display_show', update.id)
    if request.method == 'GET':
        return redirect('showlist')

def destroy(request, showid):
    if request.method == 'GET':
        showinfo = Shows.objects.get(id=showid)
        context = {
            "showinformation" : showinfo,
            "pagetitle" : f"Delete { showinfo.title }"
        }
        return render(request, 'html/confirm_delete.html', context)
    if request.method == 'POST':
        byebye = Shows.objects.get(id=showid)
        byebye.delete()
        messages.success(request, f"{ byebye.title } deleted successfully from database.")
        return redirect('showlist')

def title_check(request):
    found = False
    result = Shows.objects.filter(title=request.form['showtitle'])
    if result:
        found = True
    context = {
        "found" : found
    }
    return render(request, 'partials/titlecheck.html', context)
