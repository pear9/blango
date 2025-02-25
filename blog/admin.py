from django.contrib import admin


# Register your models here.
from blog.models import Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

from .models import *
# Register your models here.
admin.site.register(Comment)
admin.site.register(Post)
