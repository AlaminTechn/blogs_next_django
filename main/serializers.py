from rest_framework import serializers
from . models import Blogs


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = ['id', 'title', 'user', 'description', 'image',
                  'created_at', 'updated_at', 'is_published', 'is_activate']

    def validate_image(self, value):
        # resize image
        return value
