# materials = {}
# key_materials = {}
# junk = {}
# lst = input().split()
# is_obtained = False
# while True:
#     for i in range(0, len(lst), 2):
#         item = lst[i + 1].lower()
#         quantity = int(lst[i])
#         if item in materials:
#             materials[item] += quantity
#         else:
#             materials[item] = quantity
#         if item == 'motes' and materials[item] >= 250:
#             materials[item] -= 250
#             print('Dragonwrath obtained!')
#             is_obtained = True
#             break
#         elif item == 'shards' and materials[item] >= 250:
#             materials[item] -= 250
#             print('Shadowmourne obtained!')
#             is_obtained = True
#             break
#         elif item == 'fragments' and materials[item] >= 250:
#             materials[item] -= 250
#             print('Valanyr obtained!')
#             is_obtained = True
#             break
#     if is_obtained:
#         break
#     lst = input().split()
#
# for key, value in materials.items():
#     if key == "fragments":
#         key_materials[key] = value
#     elif key == "motes":
#         key_materials[key] = value
#     elif key == "shards":
#         key_materials[key] = value
#     else:
#         junk[key] = value
#     if "fragments" not in key_materials:
#         key = "fragments"
#         value = 0
#         key_materials[key] = value
#     elif "shards" not in key_materials:
#         key = "shards"
#         value = 0
#         key_materials[key] = value
#     elif "motes" not in key_materials:
#         key = "motes"
#         value = 0
#         key_materials[key] = value
#
# junk = sorted(junk.items(), key=lambda x: x[0])
# key_materials = sorted(key_materials.items(), key=lambda x: (-x[1],x[0]))
#
# for key, value in key_materials:
#     print(f'{key}: {value}')
# for key, value in junk:
#     print(f'{key}: {value}')


materials = input().lower().split()
key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
flag = False

while True:
    for i in range(0, len(materials), 2):
        key = materials[i + 1]
        value = int(materials[i])
        if key in key_materials:
            key_materials[key] += value
        elif key in junk_materials:
            junk_materials[key] += value
        elif key not in key_materials and key in ('shards', 'fragments', 'motes'):
            key_materials[key] = value
        else:
            junk_materials[key] = value
        if key in ('shards', 'fragments', 'motes') and key_materials[key] >= 250:
            key_materials[key] -= 250
            if key == 'shards':
                print('Shadowmourne obtained!')
            elif key == 'fragments':
                print('Valanyr obtained!')
            elif key == 'motes':
                print('Dragonwrath obtained!')
            flag = True
            break
    if flag:
        break
    materials = input().lower().split()

key_materials = dict(sorted(key_materials.items(), key=lambda s: (-s[1], s[0])))
junk_materials = dict(sorted(junk_materials.items(), key = lambda s: s[0]))

for key, value in key_materials.items():
    print(f'{key}: {value}')
for key, value in junk_materials.items():
    print(f'{key}: {value}')