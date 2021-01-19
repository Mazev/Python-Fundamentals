# nai barzoto reshenie

# divizor = int(input())
# bound = int(input())
# res = int(bound / divizor) * divizor
# print(res)

divizor = int(input())
bound = int(input())
for num in range(bound, 0, -1):
    if num % divizor == 0:
        print(num)
        break
