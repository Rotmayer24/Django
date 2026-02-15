from django.shortcuts import render, get_object_or_404
from blog.models import *
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

def post_auther(request, author_id):
    author = get_object_or_404(AppUser, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, "blog/post_auther.html", {"author": author, "posts": posts})
