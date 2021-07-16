from rest_framework.permissions import BasePermission
from .models import User


class IsEducator(BasePermission):
    allowed_user_roles = [User.EDUCATOR]
    def has_permission(self, request, view):
        return request.user.role in self.allowed_user_roles
    
class IsLearner(BasePermission):
    allowed_user_roles = [User.LEARNER]   
    def has_permission(self, request, view):
        return request.user.role in self.allowed_user_roles
    
    