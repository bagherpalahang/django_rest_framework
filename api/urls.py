from django.urls import path
from .views import ArticleList, ArticleDetail, UserDetail, UserList

app_name = 'api'

urlpatterns = [
    path("", ArticleList.as_view(), name='article_list'),
    path("user/", UserList.as_view(), name='user_list'),
    path("<slug:slug>", ArticleDetail.as_view(), name='article_detail'),   
    path("user/<int:pk>", UserDetail.as_view(), name='article_detail'),

]
