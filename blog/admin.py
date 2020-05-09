from django.contrib import admin
from .models import Blog, Category
from django.contrib.auth.models import User
# Register your models here.





class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Title',)}

class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CatAdmin)
