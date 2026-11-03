from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import CourseSerializer,LessonSerializer
from .models import Course,Lesson
# Create your views here.



class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer






