n = int(input())

positive_num = []
negative_nim = []

for i in range(n):
    nums = int(input())
    if nums >= 0:
        positive_num.append(nums)
    else:
        negative_nim.append(nums)
print(positive_num)
print(negative_nim)
print(f"Count of positives: {len(positive_num)}. Sum of negatives: {sum(negative_nim)}")