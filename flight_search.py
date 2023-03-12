import requests
from datetime import datetime, timedelta
from flight_data import FlightData

API_KEY = ""
KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_ENDPOINT_PRICE = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:

    def __init__(self):
        self.now = datetime.now().strftime("%d/%m/%Y")
        self.end = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        self.start = "SIN"

    def search(self, cityname):
        parameters = {
            "term": cityname, "location_types": "city"
        }
        headers = {
            "apikey": API_KEY
        }
        response = requests.get(url=KIWI_ENDPOINT, params=parameters, headers=headers)
        response.raise_for_status()
        data = response.json()["locations"][0]["code"]
        return data

    def get_price(self, code):
        headers = {
            "apikey": API_KEY
        }
        parameters = {
            "fly_from": self.start,
            "fly_to": code,
            "date_from": self.now,
            "date_to": self.end,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "SGD"
        }
        response = requests.get(url=KIWI_ENDPOINT_PRICE, params=parameters, headers=headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No direct flights found for {code}.")
            new_parameters = {
                "fly_from": self.start,
                "fly_to": code,
                "date_from": self.now,
                "date_to": self.end,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "max_stopovers": 1,
                "curr": "SGD"
            }
            response = requests.get(url=KIWI_ENDPOINT_PRICE, params=new_parameters, headers=headers)
            response.raise_for_status()
            try:
                data = response.json()["data"][0]
                print(data)
            except IndexError:
                print(f"No connecting flights found for {code}.")
                return None
            else:
                flight_data = FlightData(
                    data["price"],
                    data["route"][0]["cityFrom"],
                    data["route"][0]["flyFrom"],
                    data["route"][1]["cityTo"],
                    data["route"][1]["flyTo"],
                    data["route"][0]["local_departure"].split("T")[0],
                    data["route"][2]["local_departure"].split("T")[0],
                    stopovers=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.arr_name}: ${flight_data.price}")
                return flight_data
        else:
            flight_data = FlightData(
                data["price"],
                data["route"][0]["cityFrom"],
                data["route"][0]["flyFrom"],
                data["route"][0]["cityTo"],
                data["route"][0]["flyTo"],
                data["route"][0]["local_departure"].split("T")[0],
                data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.arr_name}: ${flight_data.price}")
            return flight_data



