from django.urls import path
from .views import UserRegistrationAPIView, confirm_email, ProfileListCreateAPIView, ProfileRetrieveUpdateDestroyAPIView, PersonnelListAPIView, PersonnelDetailAPIView, InvestorListAPIView, InvestorDetailAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('confirm-email/<uuid:token>/', confirm_email, name='confirm-email'),
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile-detail'),
    path('personnel/', PersonnelListAPIView.as_view(), name='personnel-list'),
    path('personnel/<int:pk>/', PersonnelDetailAPIView.as_view(), name='personnel-detail'),
    path('investors/', InvestorListAPIView.as_view(), name='investor-list'),
    path('investors/<int:pk>/', InvestorDetailAPIView.as_view(), name='investor-detail'),
]