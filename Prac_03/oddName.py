def main():
    odd_name = get_name(3)

    print('Odd Name:', odd_name)


def get_name(skip_num):
    name = input('Enter name >>>>')
    odd_name = ''
    # for char in range(skip_num - 1, len(name), skip_num):
    #     odd_name += name[char]

    return name[::skip_num]

    # return odd_name


main()
