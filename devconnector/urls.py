"""devconnector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from blog.views import index_function, post_function, posts_function
from accounts.views import login_function, profile_function, register_function, add_experience_function, create_profile_function, dashboard_function, profiles_function, add_education_function
# from accounts import urls as accounts_urls
# from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts')),
    # path('blog/', include('blog')),

    path('login/',login_function),
    path('',index_function),
    path('post/',post_function),
    path('posts/',posts_function),
    path('profile/',profile_function),
    path('register/',register_function),
    path('profiles/',profiles_function),
    path('add_experience/',add_experience_function),
    path('create_profile/',create_profile_function),
    path('dashboard/',dashboard_function),
    path('add_education/',add_education_function),
]
