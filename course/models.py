from django.db.models.deletion import CASCADE
from user.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name;
    
    

class CourseEnrollment(models.Model):
    user = models.ForeignKey(User, related_name='course_enrollment', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='course_enrollment', on_delete=models.CASCADE)
    date_of_enrollment = models.DateTimeField(auto_now_add=timezone.now())
    date_of_completion = models.DateTimeField(blank=True, null=True)    