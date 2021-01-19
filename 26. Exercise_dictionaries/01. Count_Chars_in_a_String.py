count_text = input()

my_dict = {}

for i in count_text:
    if i == ' ':
        continue
    if i not in my_dict:
        my_dict[i] = 0
    my_dict[i] += 1

for key, value in my_dict.items():
    print(f'{key} -> {value}')
