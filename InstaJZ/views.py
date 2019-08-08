from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from InstaJZ.models import Post
from django.urls import reverse_lazy

# Create your views here.
class HelloWorld(TemplateView):
    template_name = 'home.html'

class PostListView(ListView):
    model = Post
    template_name = 'posts.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class MakePostView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class EditPostView(UpdateView):
    model = Post
    fields = ['title']
    template_name = 'post_edit.html'   

class DeletePostView(DeleteView):
    model = Post
    template_name= 'delete_post.html'
    success_url = reverse_lazy('posts')