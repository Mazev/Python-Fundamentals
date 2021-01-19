palindroms = input().split(', ')


def is_palindroms(palindroms):
    for el in palindroms:
        if el == el[::-1]:
            print('True')
        else:
            print('False')


is_palindroms(palindroms)