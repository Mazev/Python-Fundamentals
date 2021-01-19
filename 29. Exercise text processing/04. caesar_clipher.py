data = input()

text = []

for el in data:
    results = ord(el)
    new_text = results + 3
    new_text = chr(new_text)
    text.append(new_text)
print(''.join(text))