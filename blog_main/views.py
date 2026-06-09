from django.shortcuts import render

from assignments.models import About, SocialLink
from blogs.models import Category, Blog

def home(request):
    """
    Renders the home page template.
    """
    #Fetching Categories and Blogs from the database can be done here and passed to the template context if needed.
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Publish').order_by('-created_at')[:5]
    posts = Blog.objects.filter(status='Publish').order_by('-created_at')[:10]
    try:
        about = About.objects.get()
    except About.DoesNotExist:
        about = None
    platform = SocialLink.objects.all()
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
        'platform': platform,
    }
    return render(request, 'home.html', context)