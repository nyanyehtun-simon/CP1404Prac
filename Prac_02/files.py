# name_file = open('name.txt', 'w')
#
# name = input('What is your name?: ')
#
# print(name, file=name_file)
# name_file.close()
#
# name_file = open('name.txt', 'r')
#
# name_var = name_file.readline()
#
# print('Your name is {}'.format(name_var))

numbers_file = open('numbers.txt', 'r')
number_list = numbers_file.readlines()

# This also solves for the extended question
total = 0
for i in number_list:
    total += float(i)

print('Total value is: {}'.format(total))