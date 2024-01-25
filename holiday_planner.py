# User defined function to calculate hotel cost and the number of nights
def hotel_cost(num_nights, nightly_cost):
    return num_nights * nightly_cost



# User defined function to calculate car rental and number of days
def car_rental(rental_days, daily_rental):
    return rental_days * daily_rental



# User defined function to get the choice of flight and the cost
def flight_cost(city_flight):
    return city_flight




# User defined function to calculate the total holiday cost wrapped in a try / execept to avoid crashes
def calculate_total_holiday_cost():

# Print flight choices to give the user clarity
    try:
        print("WELCOME TO CB'S HOLIDAY PLANNER\n")

        city_flight = int(input("COST OF PLANE TICKET: "))
        num_nights = int(input("NUMBER OF NIGHTS AT THE HOTEL: "))
        nightly_cost = float(input("DAILY COST OF HOTEL: "))
        rental_days = int(input("NUMBER OF DAYS YOU WANT RENT THE CAR: "))
        daily_rental = float(input("DAILY COST FOR CAR RENTAL: "))

        total_flight_cost = flight_cost(city_flight)
        total_hotel_cost = hotel_cost(num_nights, nightly_cost)
        total_car_rental = car_rental(rental_days, daily_rental)

        return total_flight_cost, total_hotel_cost, total_car_rental

    except ValueError:
        print("Invalid input. Please enter numeric values for nights, days, and flight cost.")
        return 0, 0, 0   # Return 0 value for invalid inputs
    except TypeError:
        print("Invalid input. Please enter numeric values for nights, days, and flight cost.")
        return 0, 0, 0



# Calculate the total based on the inputs/choices
total_flight, total_hotel, total_car_rental = calculate_total_holiday_cost()

try:

# If the returned values are not 0, print the total holiday cost and details
    if total_flight != 0:
        print("\nDetails of your holiday:")
        print(f"Flight cost: £{round(total_flight, 2)}")   # Round to round the total up to 2 decimals
        print(f"Hotel cost: £{round(total_hotel, 2)}")
        print(f"Car rental cost: £{round(total_car_rental, 2)}")

    total_cost = total_flight + total_hotel + total_car_rental
    print(f"Total holiday cost: £{round(total_cost, 2)}")

except TypeError:
    print("Invalid input. Please enter numeric values for nights, days, and flight cost.")