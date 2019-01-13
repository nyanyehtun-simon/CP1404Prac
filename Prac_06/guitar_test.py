from Prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar1 = Guitar(name=name, year=year, cost=cost)
print(guitar1)
print(guitar1.is_vantage())
print(guitar1.get_age())

another_guitar = Guitar(name='Another Guitar', year=2012, cost=1000)
print(another_guitar)
print(another_guitar.is_vantage())
print(another_guitar.get_age())