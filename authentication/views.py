from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import *

from .serializers import ProfileSerializer,UserRegistrationSerializer,PersonnelSerializer, InvestorSerializer

class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            category = serializer.validated_data.get('category')
            profile_data = {
                'user': user,
                'category': category,
                'profile_image': serializer.validated_data.get('profile_image'),
                'telephone': serializer.validated_data.get('telephone'),
                'location': serializer.validated_data.get('location'),
                'birth_date': serializer.validated_data.get('birth_date'),
            }
            Profile.objects.create(**profile_data)

            if category == Profile.INVESTOR:
                Investor.objects.create(user=user)
            elif category == Profile.PERSONNEL:
                Personnel.objects.create(user=user)

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


#Profiles
class PersonnelListAPIView(generics.ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_class = [IsAuthenticated]

class PersonnelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_class = [IsAuthenticated]

class InvestorListAPIView(generics.ListCreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_class = [IsAuthenticated]

class InvestorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    permission_class = [IsAuthenticated]

