from django.urls import path
from .views import MembershipAPIView

urlpatterns = [
    path('organizations/<int:organization_id>/add-user/', MembershipAPIView.as_view(), name='membership'),
]
