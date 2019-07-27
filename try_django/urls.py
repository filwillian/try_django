"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as authviews

from .views import (homepage, aboutpage, contactpage)
from blog.views import (blog_home, single_blog)
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', homepage, name='index'),
    path('about/', aboutpage, name='about'),
    path('contact/', contactpage, name='contact'),
    path('blog/', blog_home, name='blog'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/<int:blog_id>/', single_blog),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', authviews.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
