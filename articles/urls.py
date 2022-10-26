from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('article/', views.PostList.as_view(), name='articles'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('profile', views.profile, name='profile'),
    path('publish', views.publish, name='publish'),
    path('my_articles', views.my_articles, name='my_articles'),
    path('edit/<post_id>', views.edit_article, name='edit'),
    # path('delete/<post_id>', views.delete_post, name='delete'),
]