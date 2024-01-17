#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

ORIGIN_CITY_IATA="MUC"
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
print(sheet_data)

for sheet in sheet_data:
    print(sheet)
    if sheet["iataCode"] == "TEST":
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(f"sheet_data:\n {sheet_data}")

        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight:
        data_manager.update_price(destination["id"], flight)
    else:
        data_manager.no_flight_price_possible(destination["id"])

