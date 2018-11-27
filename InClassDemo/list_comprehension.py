# text = "This is a sentence"
#
# words = text.split()
#
# result = [word for word in words if len(word) > 3]
#
# print(result)

from operator import itemgetter


def string_comparsion(custom_list, index):
    print(chr(ord(custom_list[index][0]) + 1) + custom_list[index][1:])
    return chr(ord(custom_list[index][0]) + 1) + custom_list[index][1:]

data = [['Bob', 6], ['Derek', 7], ['Carrie', 8], ['Aaron', 9]]

data.sort(key=lambda custom_list: string_comparsion(custom_list, 0))

print(data)