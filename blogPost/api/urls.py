from django.urls import path
from .views import api_detail_view, api_update_view, api_delete_view, api_create_view, api_is_author_of_blogpost, ApiClassBasedView

app_name = 'blog'

urlpatterns = [
    path('<slug>/',api_detail_view, name='detail'),
    path('<slug>/update',api_update_view, name='update'),
    path('<slug>/delete', api_delete_view, name='delete'),
    path('create', api_create_view, name='create'),
    path('list', ApiClassBasedView.as_view(), name='list'),
    path('<slug>/is_author', api_is_author_of_blogpost, name="is_author"),

]