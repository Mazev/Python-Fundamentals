factor = int(input())
count = int(input())

elements = []
for num in range(1, count + 1):
    num *= factor
    elements.append(num)
print(elements)