numbers = []

for i in range(5):
    numbers.append(int(input('Number: ')))

print('The first number is {}'.format(numbers[0]))
print('The last number is {}'.format(numbers[len(numbers) - 1]))
print('The smallest number is {}'.format(min(numbers)))
print('The largest number is {}'.format(max(numbers)))
print('The average of numbers is {:.2f}'.format(sum(numbers) / len(numbers)))
