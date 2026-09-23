from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    path('comments/', views.CommentListCreateView.as_view(), name='comment_list'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment_detail'),

    path('likes/', views.LikeCreateView.as_view(), name='like_create'),
    path('likes/<int:pk>/', views.LikeDestroyView.as_view(), name='like_destroy'),
    path('register/', views.register_api, name='register'),
    path('login/', views.login_api, name='login'),  
]

