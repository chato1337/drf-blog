from rest_framework.routers import DefaultRouter
from blog.views import CommentViewSet, LikeViewSet, PostViewSet, TagViewSet
from django.urls import path

router = DefaultRouter()

router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'tag', TagViewSet)

urls = [
    path('like/<int:pk>/', LikeViewSet.as_view({'put': 'update'}))
]

urlpatterns = router.urls + urls