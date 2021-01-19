list_employees = input().split()
hapines = int(input())

list_employees = list(map(lambda x : int(x) * hapines, list_employees))

filtered = list(filter(lambda x: x > (sum(list_employees) / len(list_employees)), list_employees))

if len(filtered) >= len(list_employees) / 2:
    print(f'Score: {len(filtered)}/{len(list_employees)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(list_employees)}. Employees are not happy!')