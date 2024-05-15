from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Organization, Location, Contact

User = get_user_model()


class OrganizationTestCase(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin', email='admin@example.com', password='adminpass')
        self.location = Location.objects.create(addressline='123 Main St', street='Main St', city='City', state='State')
        self.contact = Contact.objects.create(telephone='1234567890', email='contact@example.com')

    def test_add_user_to_organization_as_admin(self):
        organization = Organization.objects.create(admin=self.admin_user, title='Test Organization', description='Test description', location=self.location, contact=self.contact, category='technology')
        user = User.objects.create_user(username='user', email='user@example.com', password='userpass')
        membership = organization.membership_set.create(user=user, role='admin')

        self.assertEqual(membership.user, user)
        self.assertEqual(membership.organization, organization)
        self.assertEqual(membership.role, 'admin')

    def test_add_user_to_organization_as_non_admin(self):
        organization = Organization.objects.create(admin=self.admin_user, title='Test Organization', description='Test description', location=self.location, contact=self.contact, category='technology')
        user = User.objects.create_user(username='user', email='user@example.com', password='userpass')
        membership = organization.membership_set.create(user=user, role='member')

        self.assertEqual(membership.user, user)
        self.assertEqual(membership.organization, organization)
        self.assertEqual(membership.role, 'member')
