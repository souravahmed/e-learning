from django.urls import path
from . import views

app_name='course'

urlpatterns = [
    path('create', views.create_course, name='create_course'),
    path('enroll_course', views.enroll_course, name='enroll_course'),
    path('update/<int:pk>', views.update_course, name='update_course')
    
]