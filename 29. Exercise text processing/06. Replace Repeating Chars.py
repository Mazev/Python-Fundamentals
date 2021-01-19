string = input()

index = 0
new_string = []
while index < len(string) - 1:
    if string[index] == string[index]:
        new_string.append(string[index])
        index = 0
        string = string.replace(string[index], "")

print(''.join(new_string))
