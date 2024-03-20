# from django.shortcuts import render
from django.contrib.auth.models import User
# from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly, IsOwnerOrStaffReadOnly

# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    parser_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'


class UserList(ListCreateAPIView):
    permission_classes = [IsSuperUserOrStaffReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrStaffReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer