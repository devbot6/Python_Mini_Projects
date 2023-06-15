class House:
    def __init__(self, registration_id, house_type, rental_cost, owner_name):
        self.registration_id = registration_id
        self.house_type = house_type
        self.rental_cost = rental_cost
        self.owner_name = owner_name
        self.available_dates = []

    def add_available_date(self, date):
        self.available_dates.append(date)

    def remove_available_date(self, date):
        if date in self.available_dates:
            self.available_dates.remove(date)

    def __str__(self):
        return f"House {self.registration_id}: {self.house_type} owned by {self.owner_name}, " \
               f"rental cost per night ${self.rental_cost}, available dates: {self.available_dates}"
