"""teacher_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# Importing necessary modules from Django
from django.contrib import admin  # This imports the Django admin module
from django.urls import path, include  # path is used to define URL patterns, include is used to include other URL configurations

# URL configuration for the project
urlpatterns = [
    # The 'admin/' URL is routed to the default Django admin interface
    path('admin/', admin.site.urls),  # This allows access to the Django admin site

    # The '' (empty string) URL is routed to the "portal.urls" module
    # The 'include' function is used to include the URLs from the "portal" app
    path('', include("portal.urls")),  # This defines that the root URL (i.e., '/') will be handled by the "portal" app
]

