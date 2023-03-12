from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
sheet = DataManager()
kiwi = FlightSearch()
sms = NotificationManager()
sheet.get_data()
count = 0


for city in sheet.city:
    sheet.edit_row(code=kiwi.search(city), row=count+2, column=2)
    prices = kiwi.get_price(kiwi.search(city))
    if prices and int(sheet.price[count]) > prices.price:
        message = f"Low price alert! Only ${prices.price} to fly from" \
                  f" {prices.dep_name}-{prices.dep_code} to" \
                  f" {prices.arr_name}-{prices.arr_code}, from " \
                  f"{prices.outbound} to {prices.inbound}."
        if prices.via_city:
            message += f"\n\nFlight has {prices.stopovers} stop over, via {prices.via_city}."
        sms.send_msg(message)
        link = f"https://www.google.com/travel/flights?q=Flights%20to%20{prices.arr_name}%20from%20{prices.dep_name}%20on%20{prices.outbound}%20through%20{prices.inbound}"
        sms.send_email(sheet.get_customer_emails(), message, link)
    count += 1







