from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class UserCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        # Assuming you have a named URL for the registration endpoint
        self.user_create_endpoint = reverse('user-register')
        self.test_user = {
            'username': 'username',
            'email': 'email@gmail.com',
            'password': 'superuser'
        }

    def test_user_is_created(self):
        # Send POST request to create a user
        response = self.client.post(
            self.user_create_endpoint, self.test_user, format='json')

        # Check if the response status is HTTP 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the user is actually created in the database
        user_exists = User.objects.filter(
            username=self.test_user['username']).exists()
        self.assertTrue(user_exists)


class UserLoginTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        # Assuming you have a named URL for the login endpoint
        self.user_login_endpoint = reverse('user-login')

        # Create a user to test with (use same password for both cases)
        self.user = User.objects.create_user(
            username='username', email='admin@gmail.com', password='superuser')

        # Test login data by username
        self.test_user_by_username = {
            'username': 'username',
            'password': 'superuser'
        }

        # Test login data by email
        self.test_user_by_email = {
            'username': 'admin@gmail.com',
            'password': 'superuser'
        }

    def test_login_by_email(self):
        response = self.client.post(
            self.user_login_endpoint, self.test_user_by_email, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)  # Ensure the token is returned

    def test_login_by_username(self):
        response = self.client.post(
            self.user_login_endpoint, self.test_user_by_username, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)  # Ensure the token is returned

    def test_login_fails_with_bad_credentials(self):
        """A test to fail with bad credentials"""
        bad_credentials = {
            'username': 'wrongusername',
            'password': 'wrongpassword'
        }

        response = self.client.post(
            self.user_login_endpoint, bad_credentials, format='json')

        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn('error', response.data)
