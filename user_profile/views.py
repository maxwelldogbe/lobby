from rest_framework import generics
from .models import PersonnelProfile, InvestorProfile
from .serializers import PersonnelProfileSerializer, InvestorProfileSerializer

class PersonnelProfileListAPIView(generics.ListCreateAPIView):
    queryset = PersonnelProfile.objects.all()
    serializer_class = PersonnelProfileSerializer

class PersonnelProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonnelProfile.objects.all()
    serializer_class = PersonnelProfileSerializer

class InvestorProfileListAPIView(generics.ListCreateAPIView):
    queryset = InvestorProfile.objects.all()
    serializer_class = InvestorProfileSerializer

class InvestorProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvestorProfile.objects.all()
    serializer_class = InvestorProfileSerializer
