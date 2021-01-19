number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(sum, three_num):
    return sum - three_num


def add_and_subtract(one, two, three):
    sum = sum_numbers(one, two, )
    res = subtract(sum, number_3)
    print(res)


add_and_subtract(number_1, number_2, number_3)
