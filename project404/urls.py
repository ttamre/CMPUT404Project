"""project404 URL Configuration

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
from rest_framework import routers
from unhindled import views

router = routers.DefaultRouter()
router.register(r'authors', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', include('unhindled.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('service/', include(router.urls)),
    path('service/author/<str:username>/liked', views.LikeViewSet.as_view({'get':'authorList'})),
    path('service/author/<str:username>/posts/', views.PostViewSet.as_view({'get':'list', 'post':'createPost'})),
    path('service/author/<str:username>/posts/<str:post_ID>', views.PostViewSet.as_view({'get':'retrieve', 'post':'updatePost'})),
    path('service/author/<str:username>/posts/<str:post_ID>/comments', views.CommentViewSet.as_view({'get':'list'})),
    path('service/author/<str:username>/posts/<str:post_ID>/likes', views.LikeViewSet.as_view({'get':'postList'})),
    path('service/author/<str:username>/posts/<str:post_ID>/comments/<str:comment_ID>/likes', views.LikeViewSet.as_view({'get':'commentList'})),
    path('service/auth/', include('rest_framework.urls', namespace='rest_framework')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

