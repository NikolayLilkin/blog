from re import template
from typing import List
from django.views.generic import ListView,DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
# Create your views here.
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'