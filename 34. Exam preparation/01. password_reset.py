password = input()
result = ''
line = input()
while not line == 'Done':
    data = line.split(' ')
    command = data[0]
    if command == 'TakeOdd':
        for index in range(1, len(password), 2):
            result += password[index]
        password = password.replace(password, result)
        print(result)
    elif command == 'Cut':
        index, lenght = [int(el) for el in data[1:]]
        sub_string = password[index: index + lenght]
        result = password[:index] + password[index+lenght:]
        password = password.replace(password, result)
        print(result)
    elif command == 'Substitute':
        substring,substitute = data[1:]
        result = password.replace(substring, substitute)
        if result == password:
            print("Nothing to replace!")
        print(result)
    line = input()

print(f"Your password is: {password}")

if substring in password:
    password = password.replace(substring, substitute)
    print(result)
else:
    print("Nothing to replace!")
