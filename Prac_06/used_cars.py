from Prac_06.car import Car


def main():
    my_car = Car(180, 'Sedan')
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print('** Limo **')
    limo = Car(100, 'Limo')
    limo.add_fuel(20)
    print('fuel =', limo.fuel)
    limo.drive(115)
    print('odo =', limo.odometer)
    print(limo)


main()

