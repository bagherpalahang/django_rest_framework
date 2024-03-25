from django.contrib.auth import get_user_model
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView

from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from .permissions import IsSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly, IsOwnerOrStaffReadOnly

# Create your views here.

# class ArticleList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = 'slug'

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['status', 'author__username']
    ordering_fields = ['created', 'updated']
    search_fields = [
        'author__username', 
        'author__first_name', 
        'author__last_name',
        'content', 
        'title',
    ]

    
    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


# class UserList(ListCreateAPIView):
#     permission_classes = [IsSuperUserOrStaffReadOnly]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsOwnerOrStaffReadOnly]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class RevokeToken(APIView):
#     permission_classes = [IsAuthenticated]

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)
    
class UserViewSet(ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsSuperUserOrStaffReadOnly,)