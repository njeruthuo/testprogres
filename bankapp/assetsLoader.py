import os
import django


# Set up Django environment
# Replace with your project name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bankapp.settings')
django.setup()


endpoint = "https://settings.bluetrax.co.ke/api/Bankapp/GetBankAssets?DateModified=2024-09-09 16:30:41.581131"

import time
import requests
import schedule
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from asset.serializers import AssetRegisterSerializer
from asset.models import Asset, AssetRegister



def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Assuming the response is in JSON
    return []

# Automatically create AssetRegister objects


def auto_create_asset_register_object():
    bluetrax_data = fetch_data(endpoint)

    print(bluetrax_data)

    # Loop through each asset from Bluetrax data
    for asset_data in bluetrax_data:
        try:
            # Check if the asset with this vehicle_reg_no exists
            asset_exists = Asset.objects.filter(
                vehicle_reg_no=asset_data["regNo"]).exists()

            if not asset_exists:
                # If asset doesn't exist, create the asset and save it
                asset = Asset.objects.create(
                    vehicle_reg_no=asset_data["regNo"],
                    make_and_model=asset_data["make_and_model"],
                    asset_value=asset_data["asset_value"],
                    purchase_price=asset_data["purchase_price"],
                    chasis=asset_data["chasis"],
                    dealer=asset_data["dealer"],
                    tracking_status=asset_data["tracking_status"],
                    asset_type=asset_data["asset_type"],
                    color=asset_data["color"],
                    insurance_value=asset_data["insurance_value"],
                    engine=asset_data["engine"],
                    asset_status=asset_data["asset_status"]
                )

                # Create a new AssetRegister entry
                serializer = AssetRegisterSerializer(data={"asset": asset.id})
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(f"Serializer errors: {serializer.errors}")

        except IntegrityError as e:
            print(f"Error inserting asset: {str(e)}")
        except KeyError as e:
            print(f"Missing field in asset data: {str(e)}")


# # Schedule the task to run every 2 hours
# def schedule_task():
#     schedule.every(2).hours.do(auto_create_asset_register_object)

#     # Keep the scheduler running
#     while True:
#         schedule.run_pending()
#         time.sleep(1)


# Main execution
if __name__ == '__main__':
    print("Starting the automatic asset register updater.")
    # schedule_task()
    auto_create_asset_register_object()
