
saleAmount = float(input('Enter sale amount:'))

while saleAmount > 0:

    if saleAmount < 1000:
        bonusAmount = saleAmount / 100 * 10
    elif saleAmount >= 1000:
        bonusAmount = saleAmount / 100 * 15

    print('The amount of user bonus is: {}'.format(bonusAmount))
    saleAmount = float(input('Enter sale amount:'))
