"""olx_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<version>/rest-auth/', include('rest_auth.urls')),
    path('api/<version>/rest-auth/', include('rest_auth.urls')),
    path('api/<version>/rest-auth/registration/', include('rest_auth.registration.urls')),

    path('api/v1/', include('users.api.v1.urls')),
    path('api/v1/', include('products.api.v1.urls')),
    path('api/v1/', include('chat.api.v1.urls')),
    path('api/v1/', include('payments.api.v1.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
