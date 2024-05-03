from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import UserSerializer,UserRegistrationSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Email confirmation    
@api_view(['GET'])   
def confirm_email(request, token):
    try:
        profile = EmailConfirmation.objects.get(confirmation_token=token)
        profile.email_confirmed = True
        profile.save()
        return Response({'message': 'Email confirmed successfully'}, status=status.HTTP_200_OK)
    except EmailConfirmation.DoesNotExist:
        return Response({'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

