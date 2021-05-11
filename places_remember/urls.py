from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),

    path('about', views.about, name='about'),
    path('create', views.create, name='create'),

    path('register', views.register, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('social_django.urls')),
]