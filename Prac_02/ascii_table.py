MIN_NUM = 33
MAX_NUM = 127

char = input('Enter a character: ')

print('The ASCII code for {0} is {1}'.format(char, ord(char)))

num = int(input('Enter a number between 33 and 127: '))

while not MIN_NUM <= num <= MAX_NUM:
    print('The input number must be between {0} and {1}'.format(MIN_NUM, MAX_NUM))
    num = int(input('Enter a number between 33 and 127: '))

print('The character for {0} is {1}'.format(num, chr(num)))

for i in range(MIN_NUM, MAX_NUM):
    print('{0:>3d}{1:>5s}'.format(i, chr(i)))

num_cols = int(input('How many columns do you want to print?: '))
for i in range(MIN_NUM, MAX_NUM + 1):
    if num_cols == 1:
        print('{0:>3d}'.format(i))
    elif num_cols == 2:
        print('{0:>3d}{1:>5s}'.format(i, chr(i)))
