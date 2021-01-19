numbers = input().split()
numbers = list(numbers)

new_list = []
asd = input()
while asd != 'END':
    token = asd.split()
    command = token[0]
    if command == 'Change':
        painting_1 = token[1]
        painting_2 = token[2]
        if painting_1 in numbers:
            painting_1= numbers.index(painting_1)
            numbers[painting_1] = numbers[painting_2]
    elif command == 'Hide':
        painting_1 = token[1]
        if painting_1 in numbers:
            numbers.remove(painting_1)
    elif command == 'Switch':
        painting_1 = token[1]
        painting_2 = token[2]
        if painting_1 in numbers:
            painting_1, painting_2 = numbers.index(painting_1), numbers.index(painting_2)
            numbers[painting_1], numbers[painting_2] = numbers[painting_2], numbers[painting_1]
    elif command == 'Insert':
        painting_1 = token[1]
        painting_2 = token[2]
        painting_1 = int(painting_1)
        painting_1 = int(painting_1)
        numbers.insert(painting_1 + 1, painting_2)
        if painting_1 > len(numbers):
            break
    elif command == 'Reverse':
        numbers.reverse()
    asd = input()



print(*numbers)
