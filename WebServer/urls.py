"""WebServer URL Configuration

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
from api.APIatUser import *
from api.APIatVideo import *
from django.http import HttpRequest

request = HttpRequest()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', UserAPI.as_view()),
    path('api/login/', LoginAPI.as_view()),
    path('api/register/', RegisterAPI.as_view()),
    path('api/follow/', FollowAPI.as_view()),
    path('api/fans/', FansAPI.as_view()),
    path('api/collection/', CollectionAPI.as_view()),
    path('api/video/', VideoAPI.as_view()),
    path('api/video/play/', PlayAPI.as_view()),
    path('api/video/like/', LikeVideoAPI.as_view()),
    path('api/video/collect/', CollectVideoAPI.as_view()),
    path('api/search/video/', SearchVideoAPI.as_view()),
    path('api/search/user/', SearchUserAPI.as_view()),
    path('api/comment/', CommentAPI.as_view()),
    path('api/reply/', ReplyAPI.as_view()),
]
