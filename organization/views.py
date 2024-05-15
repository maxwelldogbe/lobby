from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Organization, Membership
from .serializers import MembershipSerializer
from .permissions import IsOrganizationAdmin

class MembershipAPIView(generics.CreateAPIView):
    serializer_class = MembershipSerializer
    permission_classes = [IsAuthenticated, IsOrganizationAdmin]

    def post(self, request, *args, **kwargs):
        organization_id = self.kwargs.get('organization_id')
        try:
            organization = Organization.objects.get(pk=organization_id)
        except Organization.DoesNotExist:
            return Response({"error": "Organization not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the user making the request is an admin of the organization
        if organization.admin != request.user:
            return Response({"error": "You are not authorized to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organization=organization)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
