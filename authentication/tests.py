# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Profile, EmailConfirmation, Company, Personnel, Investor


# class ModelTestCase(TestCase):
#      def setUp(self):
#          # Create a test user
#          self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')

#          # Create instances of other models
#          self.profile = Profile.objects.create(
#              user=self.user,
#              profile_image='path/to/image.jpg',
#              telephone='1234567890',
#              bio='Test bio',
#              location='Test location',
#              birth_date='2000-01-01',
#              category='investor'
#          )

#          self.email_confirmation = EmailConfirmation.objects.create(
#              user=self.user,
#              email_confirmed=False
#          )

#          self.company = Company.objects.create(
#              name='Test Company',
#              date_started='2020-01-01',
#              date_ended='2022-01-01',
#              role='manager'
#          )

#          self.personnel = Personnel.objects.create(
#              user=self.user,
#              company=self.company,
#              field='Test Field',
#              skills='Test Skills'
#          )

#          self.investor = Investor.objects.create(
#              user=self.user,
#              industry='technology'
#          )

#      def test_profile(self):
#          self.assertEqual(self.profile.user.username, 'testuser')
#          self.assertEqual(self.profile.telephone, '1234567890')
#          # Add more assertions for profile fields

#      def test_email_confirmation(self):
#          self.assertEqual(self.email_confirmation.user.username, 'testuser')
#          self.assertFalse(self.email_confirmation.email_confirmed)
#          # Add more assertions for email confirmation fields

#      def test_company(self):
#          self.assertEqual(self.company.name, 'Test Company')
#          # Add more assertions for company fields

#      def test_personnel(self):
#          self.assertEqual(self.personnel.user.username, 'testuser')
#          self.assertEqual(self.personnel.company.name, 'Test Company')
#          # Add more assertions for personnel fields

#      def test_investor(self):
#          self.assertEqual(self.investor.user.username, 'testuser')
#          self.assertEqual(self.investor.industry, 'technology')
#          # Add more assertions for investor fields


# from datetime import datetime
# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Profile, EmailConfirmation, Company, Personnel, Investor


# class ProfileTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='test_user', email='test@example.com', password='testpassword')
#         self.profile = Profile.objects.create(user=self.user, telephone='123456789', bio='Test bio', location='Test location', birth_date=datetime(2000,1,1), category=Profile.PERSONNEL)

#     def test_profile_creation(self):
#         self.assertEqual(self.profile.user.username, 'test_user')
#         self.assertEqual(self.profile.telephone, '123456789')
#         self.assertEqual(self.profile.bio, 'Test bio')
#         self.assertEqual(self.profile.location, 'Test location')
#         self.assertEqual(self.profile.birth_date.strftime('%Y-%m-%d'), '2000-01-01')
#         self.assertEqual(self.profile.category, Profile.PERSONNEL)


# class EmailConfirmationTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='test_user', email='test@example.com', password='testpassword')
#         self.email_confirmation = EmailConfirmation.objects.create(user=self.user, email_confirmed=False)

#     def test_email_confirmation_creation(self):
#         self.assertEqual(self.email_confirmation.user.username, 'test_user')
#         self.assertFalse(self.email_confirmation.email_confirmed)


# class CompanyTestCase(TestCase):
#     def setUp(self):
#         self.company = Company.objects.create(name='Test Company', date_started=datetime(2020,1,1), date_ended=datetime(2021,1,1), role='manager')

#     def test_company_creation(self):
#         self.assertEqual(self.company.name, 'Test Company')
#         self.assertEqual(self.company.date_started.strftime('%Y-%m-%d'), '2020-01-01')
#         self.assertEqual(self.company.date_ended.strftime('%Y-%m-%d'), '2021-01-01')
#         self.assertEqual(self.company.role, 'manager')


# class PersonnelTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='test_user', email='test@example.com', password='testpassword')
#         self.company = Company.objects.create(name='Test Company', date_started=datetime(2020,1,1), date_ended=datetime(2021,1,1), role='manager')
#         self.personnel = Personnel.objects.create(user=self.user, company=self.company, field='Test Field', skills='Test Skills')

#     def test_personnel_creation(self):
#         self.assertEqual(self.personnel.user.username, 'test_user')
#         self.assertEqual(self.personnel.company.name, 'Test Company')
#         self.assertEqual(self.personnel.field, 'Test Field')
#         self.assertEqual(self.personnel.skills, 'Test Skills')


# class InvestorTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='test_user', email='test@example.com', password='testpassword')
#         self.investor = Investor.objects.create(user=self.user, industry='technology')

#     def test_investor_creation(self):
#         self.assertEqual(self.investor.user.username, 'test_user')
#         self.assertEqual(self.investor.industry, 'technology')



from django.contrib.auth.models import User
from django.test import TestCase
from authentication.models import Profile, Personnel, Investor, Company
from authentication.serializers import ProfileSerializer, UserRegistrationSerializer, CompanySerializer, PersonnelSerializer, InvestorSerializer


class ProfileSerializerTest(TestCase):
    def test_profile_serializer(self):
        user = User.objects.create(username='test_user', email='test@example.com', password='testpassword')
        profile = Profile.objects.create(user=user, telephone='123456789', bio='Test bio', location='Test location', birth_date='2000-01-01', category=Profile.PERSONNEL)
        serializer = ProfileSerializer(profile)
        expected_data = {
            'user': user.id,
            'profile_image': None,
            'telephone': '123456789',
            'bio': 'Test bio',
            'location': 'Test location',
            'birth_date': '2000-01-01',
            'category': Profile.PERSONNEL
        }
        self.assertEqual(serializer.data, expected_data)


class UserRegistrationSerializerTest(TestCase):
    def test_user_registration_serializer(self):
        data = {'username': 'test_user', 'email': 'test@example.com', 'password': 'testpassword', 'category': Profile.PERSONNEL}
        serializer = UserRegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))
        self.assertEqual(user.profile.category, Profile.PERSONNEL)


class CompanySerializerTest(TestCase):
    def test_company_serializer(self):
        company = Company.objects.create(name='Test Company', date_started='2020-01-01', date_ended='2021-01-01', role='manager')
        serializer = CompanySerializer(company)
        expected_data = {
            'id': '1',
            'name': 'Test Company',
            'date_started': '2020-01-01',
            'date_ended': '2021-01-01',
            'role': 'manager'
        }
        self.assertEqual(serializer.data, expected_data)


class PersonnelSerializerTest(TestCase):
    def test_personnel_serializer(self):
        company = Company.objects.create(name='Test Company', date_started='2020-01-01', date_ended='2021-01-01', role='manager')
        personnel = Personnel.objects.create(user=User.objects.create(username='test_user', email='test@example.com', password='testpassword'), company=company, field='Test Field', skills='Test Skills')
        serializer = PersonnelSerializer(personnel)
        expected_data = {
            'user': personnel.user.id,
            'company': {
                'name': 'Test Company',
                'date_started': '2020-01-01',
                'date_ended': '2021-01-01',
                'role': 'manager'
            },
            'field': 'Test Field',
            'skills': 'Test Skills'
        }
        self.assertEqual(serializer.data, expected_data)


class InvestorSerializerTest(TestCase):
    def test_investor_serializer(self):
        investor = Investor.objects.create(user=User.objects.create(username='test_user', email='test@example.com', password='testpassword'), industry='technology')
        serializer = InvestorSerializer(investor)
        expected_data = {
            'user': investor.user.id,
            'industry': 'technology'
        }
        self.assertEqual(serializer.data, expected_data)
