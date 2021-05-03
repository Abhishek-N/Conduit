from rest_framework.response import Response
from conduit.api.auth.serializers import AuthenticationSerializer
from rest_framework.decorators import action
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class AuthenticationViewset(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = AuthenticationSerializer

    def create(self, request):
        user = request.data.get('user')
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        id = serializer.data.get('id')
        user_obj = User(email=id)
        
        refresh = RefreshToken.for_user(user_obj)
        token = {'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        
        return Response({'user': {**serializer.data, 'token': token}}, status=status.HTTP_201_CREATED)