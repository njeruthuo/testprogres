import requests
import time
from django.core.management.base import BaseCommand
from asset.models import Asset, AssetRegister
from asset.serializers import AssetRegisterSerializer
from django.db.utils import IntegrityError

from clients.models import Client
from loan.models import Loan
from remedial.models import Remedial
from requests.exceptions import ChunkedEncodingError, ConnectionError

# Endpoint to fetch data
endpoint = "https://settings.bluetrax.co.ke/api/Bankapp/GetBankAssets?DateModified=2024-09-09 16:30:41.581131"


def fetch_data(url, retries=3, timeout=10):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()  # Check for HTTP errors
            return response.json()
        except (ChunkedEncodingError, ConnectionError) as e:
            attempt += 1
            print(f"Error fetching data: {e}. Retrying {attempt}/{retries}...")
            time.sleep(2)  # Wait for 2 seconds before retrying
        except requests.exceptions.Timeout:
            print("Request timed out. Retrying...")
            attempt += 1
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data: {e}")
            break
    return []


def auto_create_asset_register_object():
    bluetrax_data = fetch_data(endpoint)

    for asset_data in bluetrax_data:
        try:
            asset_exists = Asset.objects.filter(
                vehicle_reg_no=asset_data["asset_name"]).exists()

            if not asset_exists:
                asset = Asset.objects.create(
                    vehicle_reg_no=asset_data["asset_name"],
                    make_and_model=f"{asset_data['make']} {asset_data['model']}",
                    asset_value=0,
                    purchase_price=0,
                    chasis="",
                    dealer="",
                    tracking_status="",
                    asset_type="",
                    color="",
                    insurance_value=0,
                    engine="",
                    asset_status=asset_data["assetStatuses"]["description"]
                )

                client = Client.objects.create(
                    first_name="",
                    last_name="",
                    company_name=asset_data["ownership"],
                    id_number=0,
                    mobile_number="",
                    email_address="",
                    PIN_number=""
                )

                loan = Loan.objects.create(
                    # loan_batch_number=0,
                    deposit_amount=0,
                    loan_amount=0,
                    loan_status="",
                    # loan_start_date=None,
                    # loan_end_date=None,
                    # loan_period=None,
                    # loan_requirements=[]
                )
                remedial = Remedial.objects.create(
                    tracking_vendor="",
                    repossession_vendor="",
                    # date_of_repossession=None,
                    history_log=""
                )

                # serializer = AssetRegisterSerializer(
                #     data={"asset": asset.id, "client": client.id, 'loan': loan.id, 'remedial': remedial.id})
                # if serializer.is_valid():
                #     serializer.save()
                # else:
                #     print(f"Serializer errors: {serializer.errors}")

                AssetRegister.objects.create(
                    asset=asset, client=client, loan=loan, remedial=remedial)

        except IntegrityError as e:
            print(f"Error inserting asset: {str(e)}")
        except KeyError as e:
            print(f"Missing field in asset data: {str(e)}")


class Command(BaseCommand):
    help = 'Load assets from Blutrax API and insert into the AssetRegister model'

    def handle(self, *args, **kwargs):
        auto_create_asset_register_object()
        self.stdout.write(self.style.SUCCESS('Successfully loaded assets.'))
