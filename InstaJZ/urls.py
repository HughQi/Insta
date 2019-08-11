"""Insta URL Configuration

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
from django.urls import path, include

from InstaJZ.views import HelloWorld, PostListView, PostDetailView, MakePostView, EditPostView, DeletePostView, SignUp

urlpatterns = [
    path('', HelloWorld.as_view(), name='helloworld'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='postdetail'),
    path('posts/new/', MakePostView.as_view(), name='makepost'),
    path('posts/edit/<int:pk>/', EditPostView.as_view(), name='editpost'),
    path('posts/delete/<int:pk>/', DeletePostView.as_view(), name='deletepost'),
    path('auth/signup', SignUp.as_view(), name='signup'),
]