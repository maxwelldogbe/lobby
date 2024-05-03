from django.urls import path
from .views import PersonnelProfileListAPIView, PersonnelProfileDetailAPIView, InvestorProfileListAPIView, InvestorProfileDetailAPIView

urlpatterns = [
    path('api/regular-profiles/', PersonnelProfileListAPIView.as_view(), name='regular-profile-list'),
    path('api/regular-profiles/<int:pk>/', PersonnelProfileDetailAPIView.as_view(), name='regular-profile-detail'),
    path('api/investor-profiles/', InvestorProfileListAPIView.as_view(), name='investor-profile-list'),
    path('api/investor-profiles/<int:pk>/', InvestorProfileDetailAPIView.as_view(), name='investor-profile-detail'),
]
