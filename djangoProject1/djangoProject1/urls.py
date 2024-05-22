"""djangoProject1 URL Configuration

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
from django.urls import path
import app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', app.views.user_admin, name="admin"),
    path("login/", app.views.login, name="login"),
    path("register/", app.views.register, name="register"),
    path("", app.views.index, name="index"),
    path("comment/", app.views.comment, name="comment"),
    path("picture/", app.views.pictures, name="picture"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
