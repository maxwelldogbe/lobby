from rest_framework import serializers
from django.contrib.auth.models import User
from authentication.models import Profile,Personnel, Investor, Company

class ProfileSerializer(serializers.ModelSerializer):
    # profile_image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ['user']
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class PersonnelSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Personnel
        fields = "__all__"

class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = "__all__"   
                
class UserRegistrationSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=Profile.CATEGORY_CHOICES)
    profile_image = serializers.ImageField(required=False)
    telephone = serializers.CharField(required=False, max_length=100)
    location = serializers.CharField(required=False, max_length=100)
    birth_date = serializers.DateField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'category', 'profile_image', 'telephone', 'bio', 'location', 'birth_date']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        category = validated_data.pop('category')
        profile_data = {
            'profile_image': validated_data.pop('profile_image', None),
            'telephone': validated_data.pop('telephone', ''),
            'bio': validated_data.pop('bio', ''),
            'location': validated_data.pop('location', ''),
            'birth_date': validated_data.pop('birth_date', None),
        }
        
        user = User.objects.create_user(**validated_data)
        profile = Profile.objects.create(user=user, category=category, **profile_data)

        if category == Profile.INVESTOR:
            Investor.objects.create(user=user)
        elif category == Profile.PERSONNEL:
            Personnel.objects.create(user=user)

        return user
    
