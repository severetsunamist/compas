"""compas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from residential.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_view, name='listing'),
    path('search/', search_view, name='search'),
    path('createflat', createflat_view, name='createflat'),
    path('updateflat/<int:pk>/', updateflat_view, name='updateflat'),
    path('deleteflat/<int:pk>', deleteflat_view, name='deleteflat'),
    path('deletephoto/<int:pk>', deletephoto_view, name='deletephoto'),
    path('flat/<int:pk>/', flat_view, name='flat'),
    path('signup', signup_view, name='signup'),
    path('login', login_view, name='login'),
]

if settings:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
