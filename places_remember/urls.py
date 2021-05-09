from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('about', views.about, name='about'),
    path('create', views.create, name='create'),

    path('register', views.register, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
]