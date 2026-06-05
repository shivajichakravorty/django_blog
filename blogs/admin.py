from django.contrib import admin

# Register your models here.

from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}
  list_display = ('title', 'author', 'category', 'status', 'is_featured', 'created_at')
  list_filter = ('status', 'is_featured', 'created_at')
  search_fields = ('title', 'author__username', 'category__category_name')
  ordering = ('-created_at',)


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
