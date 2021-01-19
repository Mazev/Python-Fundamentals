strings = input().split()
results = ''
for el in strings:
    results += el * len(el)
print(results)