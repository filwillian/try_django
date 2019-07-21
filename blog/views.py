from django.shortcuts import render

from .models import BlogPost

# Create your views here.
def blog_home(request):
    posts = BlogPost.objects.all()
    template_name = 'blog/home.html'
    context = {'posts': posts}
    return render(request, template_name, context)

def single_blog(request, blog_id):
    post = BlogPost.objects.get(id=blog_id)
    template_name = 'blog/post.html'
    context = {'post': post}
    return render(request, template_name, context)