from Prac_06.guitar import Guitar

print('My guitars!')

guitar_list = []
name = None

while name != '':
    name = input('Name: ')
    if name == '':
        continue
    year = int(input('Year: '))
    cost = float(input('Cost: $'))

    guitar = Guitar(name, year, cost)
    print(guitar)

    guitar_list.append(guitar)

print('There are my guitars: ')
for index, single_guitar in enumerate(guitar_list):
    print("Guitar {0:}: {1:>20} ({2:}, worth ${3:,} ({4:}))".format(index, single_guitar.name, single_guitar.year,
                                                             single_guitar.cost,
                                                             'VINTAGE' if single_guitar.is_vantage() else ''))

