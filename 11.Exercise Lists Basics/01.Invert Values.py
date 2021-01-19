text = input()
result = text.split()
test = []
for num in result:
    num = int(num)
    num *= -1
    test.append(num)
print(test)