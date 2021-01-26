gifts = input().split()

command = input()
while not command == 'No Money':
    words = command.split()
    if words[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == words[1]:
                gifts[i] = 'None'
            if i != words[1]:
                continue
    elif words[0] == 'Required':
        if len(gifts) < int(words[2]):
            break
        if int(words[2]) <= len(gifts):
            gifts.insert(int(words[2]), words[1])
            gifts.pop(int(words[2+1]))
    elif words[0] == 'JustInCase':
        gifts.pop(-1)
        gifts.append(words[1])

    command = input()
for i in gifts:
    if i == 'None':
        gifts.remove(i)
print(*gifts)
