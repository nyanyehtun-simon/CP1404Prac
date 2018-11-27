# name = 'Monty'
# money = 73.6
#
# #Output: Monty has $73.60
# print('{} has ${:.2f}'.format(name, money))


# var1 = 'Simon'
# var2 = 2400
#
# print('${1:<7,d} {0} {1}'.format(var1, var2))

# temp_file = open('tempfile.txt', 'w')
# # print('first line', file=temp_file)
# print('second line', file=temp_file)
# temp_file.close()

# input_file = open('tempfile.txt', 'r')
# # output_file = open('outputfile.txt', 'w')
#
# # for line_str in input_file:
# #     new_str = ''
# #     line_str = line_str.strip()
# #     for char in line_str:
# #         new_str = char + new_str
# #     print(new_str, file=output_file)
# #
# #     print('Line: {:12s} reversed is {:s}'.format(line_str, new_str))
#
# temp_str = ''
# input_file.readline()
# input_file.readline()
#
# test_line = input_file.readline()
# if test_line == '':
#     print('this is a blank line')
# else:
#     print(ord(test_line))


import random
print(random.randint(5, 20)) # line 1
print(random.randrange(3, 10, 2)) # line 2
print(random.uniform(2.5, 5.5)) # line 3r