from rest_framework.routers import DefaultRouter
from blog.views import CommentViewSet, PostViewSet, TagViewSet

router = DefaultRouter()

router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'tag', TagViewSet)

urlpatterns = router.urls