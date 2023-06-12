from .models import Comment
from rest_framework import viewsets
from .serializers import CommentSerializer
from permissions.permissions import get_perm


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        return get_perm(self)
