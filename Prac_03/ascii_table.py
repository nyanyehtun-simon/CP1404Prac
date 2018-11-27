def get_number(lower, upper):
    num = 0

    while not lower <= num <= upper:
        try:
            num = int(input('Enter a number ({0} - {1}): '.format(lower, upper)))

            if not lower <= num <= upper:
                print('Please enter valid number')
        except ValueError:
            print('Please enter valid number')
    return num


def main():
    MIN_NUM = 33
    MAX_NUM = 127

    # char = input('Enter a character: ')
    #
    # print('The ASCII code for {0} is {1}'.format(char, ord(char)))

    num = get_number(MIN_NUM, MAX_NUM)

    # while not MIN_NUM <= num <= MAX_NUM:
    #     print('The input number must be between {0} and {1}'.format(MIN_NUM, MAX_NUM))
    #     num = int(input('Enter a number between 33 and 127: '))

    print('The character for {0} is {1}'.format(num, chr(num)))

    # for i in range(MIN_NUM, MAX_NUM):
    #     print('{0:>3d}{1:>5s}'.format(i, chr(i)))
    #
    # num_cols = int(input('How many columns do you want to print?: '))
    # for i in range(MIN_NUM, MAX_NUM + 1):
    #     if num_cols == 1:
    #         print('{0:>3d}'.format(i))
    #     elif num_cols == 2:
    #         print('{0:>3d}{1:>5s}'.format(i, chr(i)))


main()
