from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from app_user import views as v1
from app_post import views as v2
from app_comment import views as v3

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'user', v1.UserViewSet)
router.register(r'post', v2.PostViewSet)
router.register(r'comment', v3.CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)