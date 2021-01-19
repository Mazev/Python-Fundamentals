list_of_numbers = list(map(int, input().split(', ')))

max_num = list(map(int, list_of_numbers))

for i in range(1, max(max_num) // 10 + 1):
    result = [max_num[j] for j in range(len(max_num)) if max_num[j] in range(i * 10 - 10 + 1, i * 10 + 1)]
    print(f"Group of {i * 10}'s: {result}")

n = input().split(", ")
nums = list(map(int, n))

for i in range(1, max(nums) // 10 + 1):
    result = [nums[j] for j in range(len(nums)) if nums[j] in range(i * 10 - 10 + 1, i * 10 + 1)]
    print(f"Group of {i * 10}'s: {result}")
#
#

# list_of_numbers = input().split(', ')
#
# num = list(map(int, list_of_numbers))
# max_num = max(num)
# groups_count = max_num // 10
# new_list = []
#
# while True:
#     boundary = groups_count * 10
#     if num < boundary:
#         new_list.append(num)
#     print(f"Group of {boundary}'s: {new_list}")
#     new_list.clear()
