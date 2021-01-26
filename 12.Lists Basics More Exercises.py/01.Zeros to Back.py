# number = input().split(', ')
# num = list(map(int, number))
#
#
# for i in range(len(num)):
#     if num[i] == 0:
#         num.pop(i)
#         num.append(0)
# print(num)


nums = input().split(', ')
zeros = nums.count('0')

while zeros:
    nums.remove('0')
    nums.append('0')
    zeros -= 1

for num in range(len(nums)):
    nums[num] = int(nums[num])

print(nums)