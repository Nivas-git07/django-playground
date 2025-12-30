from django.urls import path
from . import views
from . import post

app_name = "blog"

urlpatterns = [
    path( "" , views.index, name="index" ),
    path("post/<int:post_id>" , post.post, name="post"),
    path("oldpath/" , post.old_redirect , name = "oldpage"),
    path("new_url/" , post.new_path , name = "newpage"),
    path("home/" , post.homepage ,  name = "homepage")
]
