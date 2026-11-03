from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from courses.models import Course,Lesson



class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(),
                                                   source='course',
                                                   write_only=True)
    class Meta:
        model = Lesson
        fields = ['id','lesson','course','course_id']


