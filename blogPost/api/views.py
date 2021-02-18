from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BlogSerializer
from blogPost.models import BlogPost


# Create view for GET request of the API
@api_view(['GET', ])
def api_detail_view(request, slug):
    try:
        post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BlogSerializer(post)
        return Response(serializer.data)