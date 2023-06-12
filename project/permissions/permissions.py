from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id or request.user.is_staff

class Forbid(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return False

def get_perm(self):
    if self.action in ['list', 'retrieve']:
        permission_classes = [permissions.AllowAny]
    elif self.action == 'create':
        permission_classes = [permissions.IsAuthenticated]
    elif self.action in ['update', 'partial_update', 'destroy']:
        permission_classes = [IsOwnerOrAdmin]
    else:
        permission_classes = [Forbid]
    return [permission() for permission in permission_classes]