from django.urls import path, re_path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('update/', views.edit_account_view, name='update'),
    path('', views.must_authenticate_view, name='must_authenticate'),

]
