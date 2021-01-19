num_wagons = int(input())

list_wagons = [0] * num_wagons
command = input()
while command != 'End':
    token = command.split()

    if token[0] == 'add':
        number_of_people = int(token[1])
        list_wagons[-1] += number_of_people
    elif token[0] == 'insert':
        index = int(token[1])
        number_of_people = int(token[2])
        list_wagons[index] += number_of_people
    elif token[0] == 'leave':
        index = int(token[1])
        number_of_people = int(token[2])
        list_wagons[index] -= number_of_people
    command = input()

print(list_wagons)
