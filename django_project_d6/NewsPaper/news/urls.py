from django.urls import path
from .views import PostsList, PostDetail, PostsSearch, PostCreateNW, PostCreateAR, PostUpdateNW, PostUpdateAR, \
    PostDelete, subscriptions

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', PostsSearch.as_view(), name='search'),
    path('news/create/', PostCreateNW.as_view(), name='news_create'),
    path('articles/create/', PostCreateAR.as_view(), name='articles_create'),
    path('news/<int:pk>/update/', PostUpdateNW.as_view(), name='news_update'),
    path('articles/<int:pk>/update/', PostUpdateAR.as_view(), name='articles_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
