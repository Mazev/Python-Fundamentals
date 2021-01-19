shoping_list = input().split('!')

new_list = []

token = input()
while token != 'Go Shoping':
    data = token.split()
    command = data[0]
    item = data[1]
    new_item  = data[2]
    if command == 'Urgent':
        new_list.append(new_item)
    elif command == 'Unnecessary':
        if new_item in shoping_list:
            shoping_list.remove(new_item)

    elif command == 'Correct':
        for i in range(len(shoping_list)):
            if [i] == item:
              shoping_list[i] = new_item[2]

    elif command == 'Rearrange':
        pass

    token = input()