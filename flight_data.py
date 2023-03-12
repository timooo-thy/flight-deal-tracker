class FlightData:

    def __init__(self, price, dep_name, dep_code, arr_name, arr_code, outbound, inbound, stopovers=1, via_city=""):
        self.price = price
        self.dep_name = dep_name
        self.dep_code = dep_code
        self.arr_code = arr_code
        self.arr_name = arr_name
        self.outbound = outbound
        self.inbound = inbound
        self.stopovers = stopovers
        self.via_city = via_city



