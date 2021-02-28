from django.urls import path,re_path
from . import views

app_name = 'home'

urlpatterns = [
    path('api/', views.api_view, name='api'),
]