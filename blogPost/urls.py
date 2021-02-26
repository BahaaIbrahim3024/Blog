from django.urls import path, re_path
from . import views

app_name = 'blogpost'
urlpatterns = [
    path('create/', views.create_blog_view, name='create'),
    path('<slug>/', views.detail_blog_view, name='detail'),
    path('<slug>/update', views.update_blog_view, name='update'),
    path('<slug>/delete/', views.delete_blog_view, name='delete'),
    path('<slug>/favorite/', views.favorite_view, name='favorite'),

]
