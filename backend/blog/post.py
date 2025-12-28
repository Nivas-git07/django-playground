from django.http import HttpResponse
from django.shortcuts import render , redirect

def post(request , post_id):
    return HttpResponse(f"you are viewing post.  and post id is {post_id}")

def old_redirect(request):
    return redirect("index")

def new_path(request):
    return HttpResponse("this is new redirect page")

