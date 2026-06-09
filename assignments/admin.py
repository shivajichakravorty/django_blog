from django.contrib import admin
from . models import About, SocialLink

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    # Allow adding only if there are no existing About instances
    if About.objects.count() >= 1:
      return False
    return True

admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)