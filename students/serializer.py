from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'status']

    status = serializers.SerializerMethodField()

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Yosh manfiy bolishi munkin emas")
        return value

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Ism qisqa bolishi bunkin emas")
        return value

    read_only = ['id']

    def get_status(self, obj):
        if obj.age <= 18:
            return "voyaga yetmagan"
        return 'voyaga yetgan'