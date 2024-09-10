import requests

url = "https://restdev.bluetrax.co.ke/api/BankApp/getStatus"


def get_post_data(search_parameter):
    # Send POST request
    response = requests.post(url, json={'regNos': [search_parameter]})

    # Check if the response contains valid JSON data and 'data' exists
    if response.status_code == 200 and 'data' in response.json():
        data = response.json()['data']

        # Ensure 'data' has at least one item
        if len(data) > 0 and 'vehicle_status' in data[0]:
            vehicle_status = data[0]['vehicle_status']

            # Ensure 'vehicle_status' has at least one item
            if len(vehicle_status) > 0:
                lon = vehicle_status[0]['lon']
                lat = vehicle_status[0]['lat']

                backup_status = vehicle_status[0].get('online_status')
                main_status = vehicle_status[0].get('online_status')

                return {
                    'backup_status': backup_status,
                    'main_status': main_status,
                    'location': {'lat': lat, 'lon': lon}
                }

    # Return None if there is no valid data
    return None
