string = input()

digits = []
letters = []
other = []

for char in string:
    if char.isalpha():
        letters.append(char)
    elif char.isdigit():
        digits.append(char)
    else:
        other.append(char)
print(''.join(digits))
print(''.join(letters))
print(''.join(other))