import random

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    num_of_upper_letter = 0
    num_of_lower_letter = 0
    num_of_numeric = 0
    num_of_special_character = 0
    is_first_time_prompted = True

    generated_password = ''
    print('Select the requirements for auto-generated password')

    password_length = int(input('Enter length of the password?: '))

    # prompt for every time total letter count does not match the password length
    while (num_of_upper_letter + num_of_lower_letter + num_of_numeric + num_of_special_character) != password_length:
        # for the first time this message won't be prompted
        if not is_first_time_prompted and (num_of_upper_letter + num_of_lower_letter + num_of_numeric +
                                           num_of_special_character) != password_length:
            print('*** Characters count does not match with password length ***')

        print('Choose the characteristic of password:')

        num_of_upper_letter = int(input('How many characters do you want as upper case letter? : '))
        num_of_lower_letter = int(input('How many characters do you want as lower case letter? : '))
        num_of_numeric = int(input('How many characters do you want as numeric character? : '))
        num_of_special_character = int(input('How many characters do you want as special character? : '))

        is_first_time_prompted = False

    # backup num count of each type to different variable for validity check in is_valid_password() method
    inputted_upper_letter_count = num_of_upper_letter
    inputted_lower_letter_count = num_of_lower_letter
    inputted_numeric_letter_count = num_of_numeric
    inputted_special_letter_count = num_of_special_character

    # generate random character until letter count of different letters is equal to 0
    while num_of_upper_letter > 0 or num_of_lower_letter > 0 or num_of_numeric > 0 or num_of_special_character > 0:
        letter_option = random.randint(1, 4)  # 1 = upper letter, 2 = lower letter, 3 = numeric, 4 = special characters

        if letter_option == 1 and num_of_upper_letter > 0:
            generated_password += random.choice(UPPER_ALPHABETS)
            num_of_upper_letter -= 1
        elif letter_option == 2 and num_of_lower_letter > 0:
            generated_password += random.choice(LOWER_ALPHABETS)
            num_of_lower_letter -= 1
        elif letter_option == 3 and num_of_numeric > 0:
            generated_password += str(random.randint(0, 9))
            num_of_numeric -= 1
        elif letter_option == 4 and num_of_special_character > 0:
            generated_password += random.choice(SPECIAL_CHARACTERS)
            num_of_special_character -= 1

    # make validity check of the password
    if is_valid_password(generated_password, password_length, inputted_upper_letter_count, inputted_lower_letter_count,
                         inputted_numeric_letter_count, inputted_special_letter_count):
        print('Auto-generated password: {}'.format(generated_password))


def is_valid_password(password, length, specified_upper_count, specified_lower_count, specified_numeric_count,
                      specified_special_character_count):

    if len(password) != length:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif SPECIAL_CHARACTERS.find(char) >= 0:
            count_special += 1

    if count_lower != specified_lower_count or count_upper != specified_upper_count or \
            count_digit != specified_numeric_count \
            or count_special != specified_special_character_count:
        return False

    print('get to true condition')
    return True


main()
