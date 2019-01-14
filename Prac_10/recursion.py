
def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

# the return result will be summation of 1 for every odd positive integer (between 0 and n)
# Result: 3
# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    # if we get to zero, we're done... just return
    if n < 0:
        return
    # if we have not hit the base case (no else needed)
    # print the square of n, then do the same for n-1
    print(n ** 2)
    do_something(n - 1)

# Result: 16, 9, 4, 1, 0 (in separate lines)
do_something(4)


def calculate_blocks(rows):
    # base case
    if rows <= 0:
        return 0
    # recursive case
    return rows + calculate_blocks(rows - 1)


def build_pyramid():
    # chosen_rows = 6
    chosen_rows = int(input("How many rows is your pyramid: "))
    print("For {} rows, you need {} blocks".format(chosen_rows,
                                                   calculate_blocks(
                                                       chosen_rows)))


build_pyramid()