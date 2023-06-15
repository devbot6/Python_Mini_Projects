# Prompt user for starting odometer reading
start_odometer = float(input("Enter the starting odometer reading: "))

# Initialize variables for total distance, fuel used, and leg MPG values
total_distance = 0
total_fuel = 0
leg_mpgs = []

# Loop to get information about each leg
while True:
    # Prompt user for current odometer reading and fuel used
    input_str = input(
        "Enter the current odometer reading and fuel used (separated by a space), or press Enter to finish: ")

    # Check if user has signaled end of trip
    if input_str == "":
        break

    # Parse the input string into odometer reading and fuel used
    odometer, fuel = map(float, input_str.split())

    # Calculate the distance and MPG for this leg
    distance = odometer - start_odometer
    mpg = distance / fuel

    # Add the MPG of this leg to the list
    leg_mpgs.append(mpg)

    # Update the total distance and fuel used
    total_distance += distance
    total_fuel += fuel

    # Update the starting odometer reading for the next leg
    start_odometer = odometer

# Print the MPG for each leg and the total MPG for the trip
print("MPG for each leg:")
for i, mpg in enumerate(leg_mpgs):
    print("Leg", i + 1, "MPG:", mpg)

if total_fuel == 0:
    print("No fuel was used, so MPG is undefined.")
else:
    total_mpg = total_distance / total_fuel
    print("Total MPG for the trip:", total_mpg)
