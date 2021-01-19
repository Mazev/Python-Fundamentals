nums = list(map(lambda x: int(x), input().split(', ')))

even_nums = []
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        even_nums.append(i)
print(even_nums)