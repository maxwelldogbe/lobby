from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import EmailConfirmation

class RegistrationAndConfirmationTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        # Send a POST request to register a new user
        response = self.client.post('/auth/users/', {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        })

        # Check that the response status code is 201 (created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check that a new user has been created in the database
        self.assertTrue(User.objects.filter(username='testuser').exists())

        # Check that the user's email address is not confirmed
        self.assertFalse(EmailConfirmation.objects.filter(user__username='testuser', email_confirmed=True).exists())

        # Retrieve the confirmation token from the response data
        confirmation_token = response.data.get('confirmation_token')

        # Send a GET request to confirm the email address
        confirm_response = self.client.get(f'/confirm-email/{confirmation_token}/')

        # Check that the response status code is 200 (OK)
        self.assertEqual(confirm_response.status_code, status.HTTP_200_OK)

        # Check that the user's email address is confirmed in the database
        self.assertTrue(EmailConfirmation.objects.filter(user__username='testuser', email_confirmed=True).exists())
