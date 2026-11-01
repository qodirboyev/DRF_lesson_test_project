from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudentModelViewSet

router = DefaultRouter()
router.register('students', StudentModelViewSet)
urlpatterns = router.urls