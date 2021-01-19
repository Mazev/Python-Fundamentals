
list_of_num = input().split()
remove_num = int(input())

novo_numbers = []
for num in list_of_num:
    num = int(num)
    novo_numbers.append(num)
for i in range(remove_num):
    novo_numbers.remove(min(novo_numbers))
print(novo_numbers)


#  vtoro reshenie

# numbers = input().split()
# numbers_to_remove = int(input())
# num = list(map(int,numbers))
#
# for i in range(numbers_to_remove):
#     num.remove(min(num))
# print(num)