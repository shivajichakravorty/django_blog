from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog


# Create your views here.

def posts_by_category(request, category_id):
  posts = Blog.objects.filter(category_id=category_id, status='Publish').order_by('-created_at')
  context = {
    'posts': posts,
  }
  return render(request, 'posts_by_category.html', context)

# Need to create the above HTML template to display the posts by category. The template should loop through the 'posts' context variable and display the relevant information for each post, such as title, author, created_at, etc.
