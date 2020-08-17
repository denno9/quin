from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'date_added',
        'published',

    ]
    list_editable=['published']
    date_hierarchy = 'date'

admin.site.register(BlogPost,BlogPostAdmin)
