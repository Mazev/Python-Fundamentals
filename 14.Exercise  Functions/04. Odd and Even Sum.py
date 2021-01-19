num = input()


def odd_and_even_sum(number):
    odd = []
    even = []
    for el in number:
        el = int(el)
        if el % 2 == 0:
            a = even.append(el)
        else:
            b = odd.append(el)
    print(f'Odd sum = {sum(odd)}, Even sum = {sum(even)}')


odd_and_even_sum(num)
