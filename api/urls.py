from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import ArticleList, ArticleDetail, UserDetail, UserList, RevokeToken

app_name = 'api'

urlpatterns = [
    path("", ArticleList.as_view(), name='article_list'),
    path("user/", UserList.as_view(), name='user_list'),
    # path("revoke-token/", RevokeToken.as_view(), name='revoke token'),
    # path('token-auth/', obtain_auth_token),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('rest-auth/', include('dj_rest_auth.urls')),

    path("<slug:slug>/", ArticleDetail.as_view(), name='article_detail'),   
    path("user/<int:pk>/", UserDetail.as_view(), name='article_detail'),

]
