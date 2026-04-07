from django.shortcuts import render, get_object_or_404
from .models import Post 

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post
    }
    return render(request, 'blog_app/post_detail.html', {'post': post})


# Create your views here.
