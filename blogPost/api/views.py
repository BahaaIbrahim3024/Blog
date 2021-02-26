from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import BlogSerializer, BlogPostUpdateSerializer, BlogPostCreateSerializer
from blogPost.models import BlogPost
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from account.models import Account
# imports for Restricting access with permissions.
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter


# Create view for GET request of the API using Function based views
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def api_detail_view(request, slug):
    try:
        post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response({'response': "This post doesn't exist or deleted"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BlogSerializer(post)
        return Response(serializer.data)


# a view of PUT request 'Update , edit' of the API
@api_view(['PUT', ])
# for make sure that only the author of the post is the same author with the token.
@permission_classes((IsAuthenticated, ))
def api_update_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({'response': "You don't have permission to edit that."})

    if request.method == 'PUT':
        serializer = BlogPostUpdateSerializer(blog_post, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Update Successful"
            data['pk'] = blog_post.pk
            data['title'] = blog_post.title
            data['body'] = blog_post.body
            data['slug'] = blog_post.slug
            data['date_updated'] = blog_post.date_updated
            image_url = str(request.build_absolute_uri(blog_post.image.url))
            if "?" in image_url:
                image_url = image_url[:image_url.rfind("?")]
            data['image'] = image_url
            data['username'] = blog_post.author.username
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# a view of DELETE request of the API
@api_view(['DELETE', ])
@permission_classes((IsAuthenticated, ))
def api_delete_view(request, slug):
    try:
        post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user = request.user
    if post.author != user:
        return Response({'response': "You don't have permission to delete this."})
    if request.method == 'DELETE':
        operation = post.delete()
        data = {}
        if operation:
            data['success'] = 'Delete Successful'
        else:
            data['fail'] = 'Delete Failed'
        return Response(data=data)


# a view of POST request of API for create a new Blog post
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def api_create_view(request):
    if request.method == 'POST':
        data = request.data
        data['author'] = request.user.pk
        serializer = BlogPostCreateSerializer(data=data)

        data = {}
        if serializer.is_valid():
            blog_post = serializer.save()
            data['response'] = "created"
            data['pk'] = blog_post.pk
            data['title'] = blog_post.title
            data['body'] = blog_post.body
            data['slug'] = blog_post.slug
            data['date_updated'] = blog_post.date_updated
            image_url = str(request.build_absolute_uri(blog_post.image.url))
            if "?" in image_url:
                image_url = image_url[:image_url.rfind("?")]
            data['image'] = image_url
            data['username'] = blog_post.author.username
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_is_author_of_blogpost(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    user = request.user
    if blog_post.author != user:
        data['response'] = "You don't have permission to edit that."
        return Response(data=data)
    data['response'] = "You have permission to edit that."
    return Response(data=data)



# define class for pagination (divide posts list into pages)  also use class based views
class ApiClassBasedView(ListAPIView):
    # Query all blogs into a list (create queryset)
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = PageNumberPagination

    # for Search & filtering &ordering
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'body', 'author__username')
    '''
    author__username' we want to search in a specific attribute in the author (author's username) 
    if there's a FK we use (model__particular field with in the model which is the author because it's the FK).
    '''

