from django.contrib import admin
from .models import category,blog
# Register your models here.

class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class blogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(category, blogCategoryAdmin, )
admin.site.register(blog,blogAdmin)