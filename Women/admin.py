from django.contrib import admin

# Register your models here.
from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug':('title', )} #To fill slug field automated using title field

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {'slug':('name', )} #To fill slug field automated using name field

admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)