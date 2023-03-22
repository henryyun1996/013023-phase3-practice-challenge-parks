
class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        national_park.add_trips(self)
        visitor.add_trips(self)
        Trip.all.append(self)