from .models import Asset
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AssetTestCase(APITestCase):

    def setUp(self):
        self.client = self.client_class()
        self.test_url = reverse('asset-create-list')

        self.asset_example = {
            'vehicle_reg_no': "KBS 100A",
            'make_and_model': "TOYOTA ISUZU",
            'asset_value': 200_000,
            'purchase_price': 3_000_000,
            'chasis': "XXXX",
            'dealer': "TOYOTA KENYA",
            'tracking_status': "XXX",
            'asset_type': "XXX",
            'color': "XXXX",
            'insurance_value': 2_500_000,
            'engine': "TOYOTA GREEN DEMON",
            'asset_status': "OK"
        }

    def test_create_asset_object(self):
        # Test creating an Asset object via the API
        response = self.client.post(
            self.test_url, self.asset_example, format='json')

        # Check if the asset was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check if the response matches
        self.assertEqual(
            response.data['vehicle_reg_no'], self.asset_example['vehicle_reg_no'])

    def test_list_asset_object(self):
        # Create an asset in the database
        # Unpack the dictionary to create the object
        Asset.objects.create(**self.asset_example)

        # Test fetching the list of Asset objects via the API
        response = self.client.get(self.test_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

        first_asset = response.data[0]
        self.assertEqual(first_asset['vehicle_reg_no'],
                         self.asset_example['vehicle_reg_no'])


class AssetStatusTestAPICase(APITestCase):
    def setUp(self) -> None:
        self.client = self.client_class()
        self.test_url = reverse('asset-status')

    def test_returns_valid_response(self):
        response = self.client.get(self.test_url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
