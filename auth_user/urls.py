from rest_framework.routers import DefaultRouter
from auth_user.simple_jwt import DecoratedTokenObtainPairView, DecoratedTokenRefreshView
from auth_user.views import ProfielViewSet, RoleViewSet, UserViewSet
from django.urls import path

router = DefaultRouter()

router.register(r'profile', ProfielViewSet)
router.register(r'role', RoleViewSet)
router.register(r'', UserViewSet)

urls = [
    path('token/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', DecoratedTokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = router.urls + urls