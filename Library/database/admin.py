from django.contrib import admin
from database import models 

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    search_fields = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title', 'authors','publisher', 'publication_date')
    filter_horizontal = ('authors',)
    
admin.site.register(models.Publisher)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)


