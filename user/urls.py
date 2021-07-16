from django.urls import path
from . import views
#from rest_framework.authtoken.views import obtain_auth_token
from .serializer import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)


app_name = 'user'


urlpatterns = [
    path('register', views.register, name='register'),
    path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify')
]