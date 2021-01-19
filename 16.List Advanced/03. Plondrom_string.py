strings = input().split()
searched_palindrome = input()

palindroms = []

for el in strings:
    if el == el[::-1]:
        palindroms.append(el)

print(palindroms)
print(f'Found palindrome {palindroms.count(searched_palindrome)} times')