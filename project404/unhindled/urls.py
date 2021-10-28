from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('post/', views.CreatePostView.as_view(), name='createPost'),
    path('inprogress/', views.HomeView.as_view(), name='stream'),
    path('account', views.AccountView.as_view(), name='account'),
    path('<str:user>/friends', views.ManageFriendView.as_view(), name='friends'),
    path('friend_request', views.friendRequest),
    path('<str:user>/articles/<str:pk>', views.PostView.as_view(), name='viewPost'),
    path('<str:user>/articles/<str:pk>/edit', views.UpdatePostView.as_view(), name='updatePost'),
    path('<str:user>/articles/<str:pk>/delete', views.DeletePostView.as_view(), name='deletePost'),
]
