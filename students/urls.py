from django.urls import path
from .views import Student_APIview,Student_Detail
urlpatterns = [
    path('students/', Student_APIview.as_view()),
    path('students/<int:pk>/', Student_Detail.as_view()),
]