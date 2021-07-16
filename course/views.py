from course.serializer import CourseEnrollmentSerializer, CourseSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from user.permissions import IsEducator, IsLearner
from rest_framework.permissions import IsAuthenticated
from .models import Course

# Create your views here.




@api_view(['POST'])
@permission_classes([IsAuthenticated, IsEducator])
def create_course(request):
    serialized = CourseSerializer(data=request.data)
    if(serialized.is_valid()):
        serialized.save()
        response = {'data': serialized.data, 'message': 'created successfully'}
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsEducator])
def update_course(request, pk):
    try:
        course = Course.objects.get(id=pk)
        serialized = CourseSerializer(instance=course, data=request.data)
        
        if(serialized.is_valid()):
            serialized.save()
            response = {'data': serialized.data, 'message': 'updated successfully'}
            return Response(response, status=status.HTTP_200_OK)
        
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Course.DoesNotExist:
        return Response({'message': 'course doesn\'t exsist'}, status=status.HTTP_404_NOT_FOUND)    
    

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsLearner])
def enroll_course(request):
    serialized = CourseEnrollmentSerializer(data=request.data)
    if(serialized.is_valid()):
        serialized.save()
        response = {'data': serialized.data, 'message': 'created successfully'}
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
       