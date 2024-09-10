from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse


class ClientTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = self.client_class()
        self.test_url = reverse('create-list-client')

        self.test_client_example = {
            'first_name': "Julius", 'last_name': "Njeru", 'company_name': "XXX", 'id_number': 38947109, 'mobile_number': "0768585724", 'email_address': "juliusn411@gmail.com", 'PIN_number': 38947109

        }

    def test_client_create_object_successfully(self):
        response = self.client.post(
            self.test_url, self.test_client_example, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
