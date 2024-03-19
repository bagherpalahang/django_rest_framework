# from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer

# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

class UserList(ListCreateAPIView):
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer