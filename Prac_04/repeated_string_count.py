strings = []

input_string = '\n'

while input_string != '':
    input_string = input('Enter a string: ')
    if input_string != '':
        strings.append((input_string))


set_of_string = set(strings)

repated_string_list = []

for unique_str in set_of_string:
    if strings.count(unique_str) > 1:
        repated_string_list.append(unique_str)

if len(repated_string_list) > 0:
    print('Strings repeated: ', end='')
    print(', '.join(repated_string_list))
else:
    print('No repated strings entered')
