# num = input("Enter a number: ")
# def recur_factorial(n):
#    if n == 1:
#        return n
#    elif n < 1:
#        return ("NA")
#    else:
#        return n*recur_factorial(n-1)
#
# print (recur_factorial(int(num)))


number_1 = int(input())
number_2 = int(input())


def factorial(num_1, num_2):
    result_num_1 = 1
    result_num_2 = 1
    for a in range(1, num_1 + 1):
        result_num_1 = a * result_num_1
    for b in range(1, num_2 + 1):
        result_num_2 = b * result_num_2
    return result_num_1 / result_num_2


total = factorial(number_1, number_2)
print(f'{total:.2f}')
