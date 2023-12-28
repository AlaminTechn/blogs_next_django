from django.contrib import admin
from .models import Blogs
# Register your models here.


class BlogsAdmin(admin.ModelAdmin):
    class Meta:
        model = Blogs
        fields = ('title', 'description', 'created_at')


admin.site.register(Blogs, BlogsAdmin)
