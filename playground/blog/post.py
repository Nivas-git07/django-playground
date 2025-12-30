from django.http import HttpResponse
from django.shortcuts import render , redirect

def post(request , post_id):
    return render(request, "detail.html")

def old_redirect(request):
    return redirect("index")

def new_path(request):
    return HttpResponse("this is new redirect page")

def homepage(request):
    return render(request,"index.html")