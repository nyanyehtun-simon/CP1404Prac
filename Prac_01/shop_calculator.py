num_of_items = int(input('Number of items: '))

while num_of_items < 0:
    print('Invalid number of items')
    num_of_items = int(input('Number of items: '))

total_price = 0

for i in range(1, num_of_items + 1, 1):
    total_price += float(input('Price of item: '))

if total_price > 100:
    discounted_total = total_price - (total_price * 0.1)

print('Total price for 3 items is ${:.2f}'.format(discounted_total))
