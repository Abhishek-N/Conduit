from rest_framework.response import Response
from conduit.api.auth.serializers import AuthenticationSerializer
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User


# Create your views here.

class AuthenticationViewset(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = AuthenticationSerializer

    def create(self, request):
        user = request.data.get('user')
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)