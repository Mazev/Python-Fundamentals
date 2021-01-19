string = input()

for el in range(len(string)):
    if string[el] == ':':
        print(f':{string[el + 1]}')