from django.shortcuts import render

def home(request):
    """
    Renders the home page template.
    """
    return render(request, 'home.html')