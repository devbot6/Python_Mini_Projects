# Define house and guest classes
class House:
    def __init__(self, reg_id, house_type, rental_cost, owner, available_dates):
        self.reg_id = reg_id
        self.house_type = house_type
        self.rental_cost = rental_cost
        self.owner = owner
        self.available_dates = available_dates
        self.renter = None

class Guest:
    def __init__(self, guest_id, name, start_date, end_date):
        self.guest_id = guest_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.rented_house = None

# Define a list to hold all houses and guests
houses = []
guests = []

# Define functions for managing house registration and rental operations
def register_house(reg_id, house_type, rental_cost, owner, available_dates):
    # Check if house with the given registration ID already exists
    for house in houses:
        if house.reg_id == reg_id:
            print("Error: House with ID {} already exists".format(reg_id))
            return

    # Create new house object and add it to the list of houses
    new_house = House(reg_id, house_type, rental_cost, owner, available_dates)
    houses.append(new_house)
    print("House with ID {} registered successfully".format(reg_id))

def unregister_house(reg_id):
    # Find the house with the given registration ID and remove it from the list of houses
    for house in houses:
        if house.reg_id == reg_id:
            if house.renter is not None:
                print("Error: House with ID {} is currently rented and cannot be unregistered".format(reg_id))
                return
            houses.remove(house)
            print("House with ID {} unregistered successfully".format(reg_id))
            return

    print("Error: House with ID {} not found".format(reg_id))

def register_guest(guest_id, name, start_date, end_date):
    # Check if guest with the given ID already exists
    for guest in guests:
        if guest.guest_id == guest_id:
            print("Error: Guest with ID {} already exists".format(guest_id))
            return

    # Create new guest object and add it to the list of guests
    new_guest = Guest(guest_id, name, start_date, end_date)
    guests.append(new_guest)
    print("Guest with ID {} registered successfully".format(guest_id))

def unregister_guest(guest_id):
    # Find the guest with the given ID and remove it from the list of guests
    for guest in guests:
        if guest.guest_id == guest_id:
            if guest.rented_house is not None:
                print("Error: Guest with ID {} has rented a house and cannot be unregistered".format(guest_id))
                return
            guests.remove(guest)
            print("Guest with ID {} unregistered successfully".format(guest_id))
            return

    print("Error: Guest with ID {} not found".format(guest_id))

def rent_house(reg_id, guest_id):
    # Find the house and guest with the given IDs
    house = None
    for h in houses:
        if h.reg_id == reg_id:
            house = h
            break

    guest = None
    for g in guests:
        if g.guest_id == guest_id:
            guest = g
            break

    # Check if both the house and guest exist
    if house is None:
        print("Error: House with ID {} not found".format(reg_id))
        return

    if guest is None:
        print("Error: Guest with ID {} not found".format(guest_id))
        return

    # Check if the house is available during the rental period
    rental_period = set(range(guest.start_date, guest.end_date + 1))
    unavailable_dates = set(house.available_dates) - set(rental_period)
    if len(unavailable_dates) != len(house.available_dates):
        print("Error: House with ID {} is not available during the rental period".format(reg_id))
        return

    # Rent the house to the guest
    house.renter = guest
    guest.rented_house = house
    print("House with ID {} rented to guest with ID {} successfully".format(reg_id, guest_id))

def return_house(reg_id):
    # Find the house with the given ID
    house = None
    for h in houses:
        if h.reg_id == reg_id:
            house = h
            break

    # Check if the house exists and is currently rented
    if house is None:
        print("Error: House with ID {} not found".format(reg_id))
        return

    if house.renter is None:
        print("Error: House with ID {} is not currently rented".format(reg_id))
        return

    # Compute the rental cost and update the house and guest objects
    rental_period = set(range(house.renter.start_date, house.renter.end_date+1))
    rental_nights = len(rental_period)
    total_rental_cost = house.rental_cost * rental_nights
    house.renter.rented_house = None
    house.renter = None
    print("House with ID {} returned successfully. Total rental cost is ${}".format(reg_id, total_rental_cost))


def report_house_info():
    # Display information for all houses
    print("**********************************************************")
    print("House Information:")
    for house in houses:
        print(" Registration ID: {}".format(house.reg_id))
        print(" House Type: {}".format(house.house_type))
        print(" Rental Cost per Night: ${}".format(house.rental_cost))
        print(" Owner's Name: {}".format(house.owner))
        print(" Available Dates: {}".format(house.available_dates))
        print(" Rented By: {}".format(house.renter.name if house.renter else "None"))
        print("**************************************************************")

def report_guest_info():
    # Display information for all guests
    print("Guest Information:")
    for guest in guests:
        print(" Guest ID: {}".format(guest.guest_id))
        print(" Name: {}".format(guest.name))
        print(" Rental Period: {} to {}".format(guest.start_date, guest.end_date))
        print(" Rented House: {}".format(guest.rented_house.reg_id if guest.rented_house else "None"))
        print("**************************************************************")


register_house("H001", "Single House", 100, "John Doe", [1, 2, 3, 4, 5, 6])
register_house("H002", "Apartment", 50, "Jane Smith", [3, 4, 5, 6, 7, 8])
register_house("H003", "Condo", 200, "Bob Johnson", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("**************************************************************")

register_guest("G001", "Alice Brown", 3, 5)
register_guest("G002", "Bob Green", 6, 8)

print("***************************************************************")

unregister_guest("G002")

print("*****************************************************************")

unregister_house("H002")

print("*******************************************************************")

rent_house("H001", "G001")
rent_house("H002", "G002")
rent_house("H003", "G002") # This should fail because H003 is not available during the rental period

print("*********************************************************************")


return_house("H001")
return_house("H002")



report_house_info()
report_guest_info()