from rest_framework.routers import DefaultRouter

from auth_user.views import ProfielViewSet, RoleViewSet

router = DefaultRouter()

router.register(r'profile', ProfielViewSet)
router.register(r'role', RoleViewSet)

urlpatterns = router.urls