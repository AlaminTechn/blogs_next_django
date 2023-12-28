from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blogs(models.Model):
    title = models.CharField(max_length=55)
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(
        upload_to="main/blogs/image", blank=True, null=True)
    is_published = models.BooleanField(default=False, blank=True, null=True)
    is_activate = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        
        db_table = 'blogs'
        verbose_name = 'Blogs'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return f"{self.title} {self.description}"
