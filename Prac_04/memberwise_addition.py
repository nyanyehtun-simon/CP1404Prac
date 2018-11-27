def memberwise_addition(list1, list2):
    # length = len(list1) if len(list1) > len(list2) else len(list2)

    # return [list1[i] + list2[i] for i in range(length)]
    # return [sum(x) for x in zip(*[list1, list2])]
    return [sum(x) for x in zip(list1, list2)]
    # return map(sum, zip(*[list1, list2]))


def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    list3 = [1, 2, 3]
    list4 = [1, 2, 3, 4]
    print('memberwiseAddition({0}, {1}) would return {2}'.format(list1, list2, memberwise_addition(list1, list2)))
    print('memberwiseAddition({0}, {1}) would return {2}'.format(list3, list4, memberwise_addition(list3, list4)))

main()