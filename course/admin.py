from django.contrib import admin

from .models import Course, CourseEnrollment

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'is_active']
    
    
@admin.register(CourseEnrollment)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course']
        
    
    

