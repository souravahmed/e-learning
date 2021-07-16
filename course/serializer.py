from django.db.models import fields
from .models import Course, CourseEnrollment
from rest_framework import serializers



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'is_active']
        extra_kwargs = {
            'id': {'read_only': True}
        }

class CourseEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = ['id', 'user', 'course']
        extra_kwargs = {
            'id': {'read_only': True}
        }        