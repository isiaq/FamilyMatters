from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('email/', views.emailView, name='email'),
	path('success/', views.successView, name='success'),
#    path('about/', views.successView, name='about'),
#    path('session/', views.successView, name='session'),
#    path('connect/', views.successView, name='connect'),
#    path('media/', views.successView, name='media'),

]
