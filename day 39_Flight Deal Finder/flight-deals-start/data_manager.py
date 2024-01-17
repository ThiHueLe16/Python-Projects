import requests
from pprint import pprint
SHEETY_GET_URL="https://api.sheety.co/9d464d54e93643d616111bc10cf215f6/flightDeals/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data={}

    def get_destination_data(self):
        response = requests.get(SHEETY_GET_URL)
        response.raise_for_status()
        self.destination_data=response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_GET_URL}/{city['id']}",
                json=new_data
            )
            # print(response.text)
    def update_price(self,id,  flightData):
            new_data = {
                "price": {
                    "lowestPrice": flightData.price
                }

            }
            response = requests.put(
                url=f"{SHEETY_GET_URL}/{id}",
                json=new_data
            )
            # print(response.text)
    def no_flight_price_possible(self, id):
        new_data = {
            "price": {
                "lowestPrice": "No flight found"
            }

        }
        response = requests.put(
            url=f"{SHEETY_GET_URL}/{id}",
            json=new_data
        )

