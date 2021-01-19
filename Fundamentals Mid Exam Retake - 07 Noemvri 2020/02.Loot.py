# in_chest = input().split('|')
# items_in_chest = list(map(str,in_chest))
#
# command = input().split()
# while not command == "Yohoho!":
#     uslovie = command
#     predmeti = command
#     if uslovie == 'Loot':
#         if not predmeti:
#             items_in_chest.insert(0,predmeti)
#         else:
#             continue
#     elif uslovie == 'Drop':
#         pass
in_chest = input().split("|")
commands = input().split()


while not commands[0] == "Yohoho!":
    command = commands[0]
    items = commands[:]

    if command == "Loot":
        if not items in in_chest:
            in_chest.insert(0, items)
        else:
            continue

    elif command == "Drop":
        item = int(items[2])


        pass
        # if (card in arsenal) and (index in range(0, len(the_deck))):
        #     the_deck.insert(index, card)
        # else:
        #     print("Error!")