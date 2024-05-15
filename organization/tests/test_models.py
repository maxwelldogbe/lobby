# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from django.contrib.auth.models import User
# from .models import Organization, Membership

# class OrganizationTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#         # Create users
#         self.admin_user = User.objects.create_user(username='admin', password='adminpassword')
#         self.non_admin_user = User.objects.create_user(username='nonadmin', password='nonadminpassword')
        
#         # Create organization
#         self.organization = Organization.objects.create(admin=self.admin_user, title='Test Organization', location='Test Location')

#     def test_add_user_to_organization_as_admin(self):
#         # Authenticate as admin user
#         self.client.force_authenticate(user=self.admin_user)
        
#         # Add user to organization
#         response = self.client.post(f'/organizations/{self.organization.id}/add-user/', {'user': self.non_admin_user.id, 'role': 'member'})
        
#         # Check response status code
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
#         # Check that the user is added to the organization
#         self.assertTrue(Membership.objects.filter(user=self.non_admin_user, organization=self.organization).exists())

#     def test_add_user_to_organization_as_non_admin(self):
#         # Authenticate as non-admin user
#         self.client.force_authenticate(user=self.non_admin_user)
        
#         # Try to add user to organization
#         response = self.client.post(f'/organizations/{self.organization.id}/add-user/', {'user': self.admin_user.id, 'role': 'member'})
        
#         # Check response status code (should be 403 Forbidden)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
#         # Check that the user is not added to the organization
#         self.assertFalse(Membership.objects.filter(user=self.admin_user, organization=self.organization).exists())

#     # Add more test cases as needed
