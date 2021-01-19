materials = {}
key_materials = {}
junk = {}
lst = input().split()
is_obtained = False
while True:
    for i in range(0, len(lst), 2):
        item = lst[i + 1].lower()
        quantity = int(lst[i])
        if item in materials:
            materials[item] += quantity
        else:
            materials[item] = quantity
        if item == 'motes' and materials[item] >= 250:
            materials[item] -= 250
            print('Dragonwrath obtained!')
            is_obtained = True
            break
        elif item == 'shards' and materials[item] >= 250:
            materials[item] -= 250
            print('Shadowmourne obtained!')
            is_obtained = True