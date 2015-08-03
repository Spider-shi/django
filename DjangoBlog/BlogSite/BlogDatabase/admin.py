from django.contrib import admin
from BlogDatabase import models

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

    
admin.site.register(models.BlogPost, BlogPostAdmin)