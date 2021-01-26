permutation = input().split()
kill_count = int(input())

new_list = []
counter = 0

index = 0
while len(permutation) > 0:
    counter +=1
    if counter % kill_count == 0:
        new_list.append(permutation.pop(index))
    else:
        index +=1
    if index >= len(permutation):
        index = 0

print(str(new_list).replace(' ', '').replace('\'', ''))