numbers = input().split(', ')
beggars_count = int(input())

money = []
for num in numbers:
    num = int(num)
    money.append(num)

beggars = []
for i in range(beggars_count):
    beggars.append(0)

index = 0
for number in money:
    beggars[index] += number
    index += 1

    if index == beggars_count:
        index = 0
print(beggars)

