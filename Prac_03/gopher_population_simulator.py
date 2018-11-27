import random
population = 1000

BIRTH_LOWER_RATE = 10
BIRTH_UPPER_RATE = 20

DEATH_LOWER_RATE = 5
DEATH_UPPER_RATE = 25

year = 1

print()
print('Welcome to the Gopher Population Simulator!')
print('Starting population: {}'.format(population))

while year <= 10:

    birth_rate = random.randint(BIRTH_LOWER_RATE, BIRTH_UPPER_RATE)
    death_rate = random.randint(DEATH_LOWER_RATE, DEATH_UPPER_RATE)

    current_year_birth_count = round(population * birth_rate / 100)
    current_year_death_count = round(population * death_rate / 100)

    population = population + current_year_birth_count - current_year_death_count

    print('Year {}'.format(year))
    print('****')
    print('{} gophers born. {} died.'.format(current_year_birth_count, current_year_death_count))
    print('Population: {}'.format(population), end='\n')

    year += 1

