from django.contrib.auth.models import User
from blog.models import BlogPost
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, PostSerializer

def homepage(request):
    return render(request, 'home.html')

def aboutpage(request):
    return render(request, 'about.html')

def contactpage(request):
    return render(request, 'contacts.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer