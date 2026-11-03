from .views import CoursesViewSet,LessonViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('', CoursesViewSet)
# urlpatterns = router.urls

router = DefaultRouter()
router.register('', LessonViewSet)
urlpatterns = router.urls