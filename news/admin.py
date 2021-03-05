from django.contrib import admin
from .models import *

# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'short_title')
    list_filter = ('title', 'short_title', )
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'category', 'status')
    list_filter = ('status', 'created', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', 'created')

    
admin.site.register(Subscribe)


@admin.register(ContactEnty)
class ContactEntyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject')
    list_filter = ('name', 'email', 'phone', 'subject')
    search_fields = ('name', 'phone', 'email')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'time')
    list_filter = ('name', 'email', 'time')
    search_fields = ('name', 'email', 'time')
    
