
from blogs.models import Category
def get_categories(request):
  categories = Category.objects.all()
  return {'categories': categories}


def get_social_links(request):
  from assignments.models import SocialLink
  social_links = SocialLink.objects.all()
  return {'social_links': social_links}