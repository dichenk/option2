from app_user.models import CustomUser
from rest_framework import viewsets
from app_user.serializers import UserSerializer

from rest_framework import permissions
from permissions.permissions import IsOwnerOrAdmin, Forbid


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [permissions.AllowAny]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsOwnerOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [Forbid]
        return [permission() for permission in permission_classes]