from rest_framework import serializers
from .models import PersonnelProfile, InvestorProfile, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['__al__']

class PersonnelProfileSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = PersonnelProfile
        fields = ['__al__']

class InvestorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorProfile
        fields = ['__al__']
