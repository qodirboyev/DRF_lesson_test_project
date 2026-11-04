from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudentModelViewSet,ProfileAPIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView



urlpatterns = [
    path('profile/', ProfileAPIView.as_view(),name='profile'),
    path('login/', TokenObtainPairView.as_view(),name='login'),
    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
]


router = DefaultRouter()
router.register('students', StudentModelViewSet)
urlpatterns += router.urls
