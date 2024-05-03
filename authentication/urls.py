from django.urls import path
from authentication.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView,UserRegistrationAPIView, confirm_email

urlpatterns = [
    path('api/user/', UserListCreateAPIView.as_view(), name='user-list'),
    path('api/user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('api/register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('confirm-email/<uuid:token>/', confirm_email, name='confirm-email'),
]
