class Visitor:

    def __init__(self, name):
        if type(name) == str and (len(name) > 0 and len(name) < 16):
            self._name = name
        self._trips = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        name

    name = property(get_name, set_name)

    def add_trips(self, trip):
        self._trips.append(trip)

    def trips(self):
        return self._trips
    
    def add_national_parks(self, national_park):
        self._national_park = []

    def national_parks(self):
        return self._national_park

    def create_trip(self, national_park, start_date, end_date):
        return Trip(self, national_park, start_date, end_date)

    