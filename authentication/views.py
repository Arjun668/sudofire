from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView   
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User
from .serializer import LoginTokenObtainPairSerializer,UserCreateSerializer,UserSerializer


class LoginApiViewset(TokenObtainPairView):
    serializer_class = LoginTokenObtainPairSerializer

    

class RegisterViewset(viewsets.ModelViewSet):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        self.serializer_class = UserSerializer
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer_obj = UserCreateSerializer(data=request.data)
        if serializer_obj.is_valid():
            user = serializer_obj.save()
            
            # Set encryted password
            user.set_password(user.password)
            user.save()
            
            
            user_info = UserSerializer(user).data
            
            # Remove Password
            user_info.pop('password')
            
            data = {'status': 'SUCCESS', 'data': user_info}
            return Response(status=200, data=data)
        else:
            data = {'status': 'FAILED', 'data': serializer_obj.errors}
            return Response(status=400, data=data)