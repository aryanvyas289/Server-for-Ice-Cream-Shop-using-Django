"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include  # Import include for including app URLs
from home import views  # Assuming 'home' is your app name

admin.site.site_header = "Aryan Ice Cream Admin Portal" #Admin Portal HEADERS AND CONTENT
admin.site.site_title = "Aryan Ice Cream Admin Portal"
admin.site.index_title = "Welcome to Aryan Ice Cream Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include app-specific URLs
]
