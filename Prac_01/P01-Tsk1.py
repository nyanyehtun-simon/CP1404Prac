"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

saleAmount = float(input('Enter sale amount:'))

if saleAmount < 1000:
    bonusAmount = saleAmount / 100 * 10
elif saleAmount >= 1000:
    bonusAmount = saleAmount / 100 * 15

print('The amount of user bonus is: {}'.format(bonusAmount))
