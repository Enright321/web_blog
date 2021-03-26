from django.shortcuts import render
from .models import Post

posts = [
  {
    'title': 'First Post',
    'author': 'Joe',
    'content': 'Hello world',
    'date_posted': 'June 7 2021'
  },
  {
    'title': 'Second Post',
    'author': 'Corey',
    'content': 'Hello world',
    'date_posted': 'June 8 2021'
  }
]

# Create your views here.
def home(request):

  context = {
    'posts': Post.objects.all(),
    'title': 'Welcome!'
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})