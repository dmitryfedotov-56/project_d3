# Create your views here.
from django.views.generic import ListView
from .models import Post, Comment



class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_name = 'post'



