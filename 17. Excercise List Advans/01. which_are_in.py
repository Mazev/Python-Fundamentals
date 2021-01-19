substring = input().split(', ')
words = input().split(', ')
result = []
for subst in substring:
    for word in words:
        if subst in word and subst not in result:
            result.append(subst)

print(result)
