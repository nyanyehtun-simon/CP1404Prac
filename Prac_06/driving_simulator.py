from Prac_06.car import Car

VALID_USER_CHOICES = ['d', 'r', 'q']

print("Let's drive!")

name = input('Enter you car name: ')
user_choice = None
distance_in_km = -1
units_of_fuel = -1
car = Car(fuel=100, name=name)


while user_choice != 'q':
    print(car)

    print("""
    Menu:
    d) drive
    r) refuel
    q) quit
    """)
    user_choice = input('Enter your choice: ').lower()

    if user_choice not in VALID_USER_CHOICES:
        print('Invalid choice')
    else:
        if user_choice == 'd':
            while distance_in_km < 0:
                distance_in_km = int(input('How many km do you wish to drive? '))

                if distance_in_km < 0:
                    print('Distance must be >= 0')

            actual_distance = car.drive(distance_in_km)
            if car.fuel == 0:
                print('The car drive {}km and run out of fuel'.format(actual_distance))
            else:
                print('The car drive {}km'.format(actual_distance))
            distance_in_km = -1
        elif user_choice == 'r':

            while units_of_fuel < 0:
                units_of_fuel = int(input('How many units of fuel do you want to add to the card?'))

                if units_of_fuel < 0:
                    print('Fuel amount must be >= 0')

            car.add_fuel(units_of_fuel)
            print('Added {} units of fuel'.format(units_of_fuel))
            units_of_fuel = -1

print("Good bye {}'s driver.".format(name))

















