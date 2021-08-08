from django.contrib import admin
from blog.models import Post
# Register your models here.
@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):
    list_display = ['id','title','description']
