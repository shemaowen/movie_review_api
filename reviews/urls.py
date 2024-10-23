from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, UserViewSet

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls