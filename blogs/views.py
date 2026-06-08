from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category


# Create your views here.

def posts_by_category(request, category_id):
  posts = Blog.objects.filter(category_id=category_id, status='Publish').order_by('-created_at')
  category = get_object_or_404(Category, id=category_id)
  # try:
  #   category = get_object_or_404(Category, id=category_id)
  # except:
  #   return redirect('home')  # Redirect to 404 if category does not exist
  context = {
    'posts': posts,
    'category': category,
  }
  return render(request, 'posts_by_category.html', context)

# Need to create the above HTML template to display the posts by category. The template should loop through the 'posts' context variable and display the relevant information for each post, such as title, author, created_at, etc.
