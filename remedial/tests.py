from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse

from datetime import date


class RemedialTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = self.client_class()
        self.test_url = reverse('remedial-create-list')

        self.test_remedial_example = {
            'tracking_vendor': "RiverCross",
            "repossession_vendor": "RiverCross",
            "date_of_repossession": date.today().isoformat(),
            "history_log": 'History Log',
        }

    def test_remedial_create_objects(self):
        response = self.client.post(
            self.test_url, self.test_remedial_example, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_remedial_lists_objects(self):
        # self.client.post(
        #     self.test_url, self.test_remedial_example, format='json')

        # response = self.client.get(self.test_url)

        # print(response.data)

        # self.assertIn(['tracking_vendor' in obj.keys() for obj in response.data], response.data)

        pass
