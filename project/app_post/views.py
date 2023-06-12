from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
from permissions.permissions import get_perm


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        return get_perm(self)