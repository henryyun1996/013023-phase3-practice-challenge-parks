from .trip import Trip

class NationalPark:
    
    def __init__(self, name):
        if type(name) == str:
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

    def visitors(self):
        return list(set(map(lambda trip: trip.visitor, self.trips())))
    
    def num_trips(self):
        return len(self._trips)