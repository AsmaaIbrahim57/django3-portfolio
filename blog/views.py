from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})
def single(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    return render(request,'blog/single.html',{'post':post})
