"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.schema import swagger_urlpatterns


profile_urls = [
    path("", include("apps.user.urls.profile")),
    path("product/", include("apps.product.urls.profile"))
    ]


api_v1_urls = [
    path("auth/", include("apps.user.urls.auth")),
    path("profile/", include(profile_urls)),
    path("product/", include("apps.product.urls.product"))
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_v1_urls)),
]


if settings.DEBUG:
    urlpatterns += [
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
        *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    ]
    urlpatterns += swagger_urlpatterns