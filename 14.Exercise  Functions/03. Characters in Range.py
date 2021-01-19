input_1 = input()
input_2 = input()


def characters_in_range(character_1, character_2):
    new_list = []
    for num in range(character_1 + 1, character_2 ):
        redy_list = new_list.append(chr(num))
    print(*new_list)


input_1 = ord(input_1)
input_2 = ord(input_2)
characters_in_range(input_1, input_2)

