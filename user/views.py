from rest_framework.response import Response
from user.serializer import UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .models import User

# Create your views here.



@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if(serializer.is_valid()):
        new_user = serializer.save();
        return Response({'data': serializer.data, 'message': 'user created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)