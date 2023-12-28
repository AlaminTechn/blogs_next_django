from django.urls import path
from .views import BlogAPIView, BlogDetailsAPIView


urlpatterns = [
    path('blogs/', BlogAPIView.as_view(),),
    path('blogs/<int:pk>', BlogDetailsAPIView.as_view(),)
]
