from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category


# Create your views here.

def posts_by_category(request, category_id):
  # Fetch posts that belong to the category with the given id
  posts = Blog.objects.filter(category_id=category_id, status='Publish').order_by('-created_at')
  # Get the category object to display its name. This will raise a 404 if the category doesn't exist.
  category = get_object_or_404(Category, pk=category_id)
  context = {
    'posts': posts,
    'category': category,
  }
  return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
  post = get_object_or_404(Blog, slug=slug, status='Publish')
  context = {
    'post': post,
  }
  return render(request, 'blog_detail.html', context)

# Need to create the above HTML template to display the posts by category. The template should loop through the 'posts' context variable and display the relevant information for each post, such as title, author, created_at, etc.
