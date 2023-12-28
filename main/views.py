from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Blogs
from .serializers import BlogSerializer

# Create your views here.


class BlogAPIView(APIView):

    def get(self, request):
        queryset = Blogs.objects.all()
        serializer = BlogSerializer(queryset, many=True)
        result = serializer.data
        return Response({"success": True, "data": result}, status=HTTP_200_OK)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=HTTP_200_OK)
        return Response({"success": False, "message": serializer.errors}, status=HTTP_400_BAD_REQUEST)


class BlogDetailsAPIView(APIView):

    def get(self, request, pk):
        blog_instance = get_object_or_404(Blogs, id=pk)
        serializers = BlogSerializer(blog_instance)
        return Response(serializers.data, status=HTTP_200_OK)

    def put(self, request, pk):
        blog_instance = get_object_or_404(Blogs, id=pk)
        serializers = BlogSerializer(blog_instance, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Data Updated Successfully ", "data": serializers.data}, status=HTTP_200_OK)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog_instance = get_object_or_404(Blogs, id=pk)
        blog_instance.delete()
        return Response({"message": "Blogs Deleted Successfully"}, status=HTTP_200_OK)
