from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modify_time', 'category', 'auth']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
# Register your models here.
