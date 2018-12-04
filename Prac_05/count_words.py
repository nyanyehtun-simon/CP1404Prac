user_input_text = ''

user_input_text = input('Enter text: ')

word_list = user_input_text.split(' ')
word_count_dict = {}

for val in word_list:
    key = val.lower()
    try:
        word_count_dict[key] += 1
    except KeyError:
        word_count_dict[key] = 1

print('*** Word Count ***')
for key in sorted(word_count_dict):
    longest_string_length = max(len(word) for word in word_count_dict.keys())
    print("{1:>{0}} = {2:}".format(longest_string_length, key, word_count_dict[key]))
