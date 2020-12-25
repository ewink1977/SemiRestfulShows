from django.shortcuts import render, redirect, HttpResponse

def newshow(request):
    return render(request, 'html/newshow.html')


