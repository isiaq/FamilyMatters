"""FamilyMatters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.urls import path
from django.views.generic import RedirectView
from bimbofamily import views

urlpatterns = [
    path('bimbofamily/', include('bimbofamily.urls')),
    path('photologue/', include('photologue.urls', namespace='photologue')),
    path('admin/', admin.site.urls),
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),
    path('', RedirectView.as_view(url='/bimbofamily/', permanent=True)),
    path('about/', views.about, name='about'),
    path('session/', views.session, name='session'),
    path('connect/', views.connect, name='connect'),
    path('memorial/', views.memorial, name='memorial'),
    
    
] 