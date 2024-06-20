from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse



# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/AllPost.html')


def single_post(request, slug):
    # post = get_object_or_404(index() , slug = slug)
    # context = {
    #     "post_title": post.title
    # }
    # return  render(request , 'blog/singlePost.html' , context)
    return render(request, 'blog/singlePost.html')
