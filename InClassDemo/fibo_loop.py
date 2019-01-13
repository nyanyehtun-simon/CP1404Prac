n_term = int(input('Enter n-term: '))

first_val = 0
second_val = 1

print('0, 1, ', end='')
for i in range(n_term - 2):
    temp_val = second_val
    second_val += first_val
    first_val = temp_val
    print(second_val, end=', ')
print()

print('Result of {} term: {}'.format(n_term, second_val))