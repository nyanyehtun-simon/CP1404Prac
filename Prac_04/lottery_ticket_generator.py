import random

MIN = 1
MAX = 45

quick_pick = int(input('How many quick picks?'))

quick_pick_list = []

for i in range(quick_pick):
    single_line_list = []

    while len(single_line_list) < 6:
        rand_num = random.randint(MIN, MAX)

        if rand_num not in single_line_list:
            single_line_list.append(rand_num)

    quick_pick_list.append(single_line_list)

for i in range(quick_pick):
    for j in range(len(quick_pick_list)):
        print('{:>3}'.format(quick_pick_list[i][j]), end='')
    print()
