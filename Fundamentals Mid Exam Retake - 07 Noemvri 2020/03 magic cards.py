arsenal = input().split(":")
commands = input().split()
the_deck = []

while not commands[0] == "Ready":
    command = commands[0]
    card = commands[1]

    if command == "Add":
        if card in arsenal:
            the_deck.append(card)
        else:
            print("Card not found.")

    elif command == "Insert":
        index = int(commands[2])
        if (card in arsenal) and (index in range(0, len(the_deck))):
            the_deck.insert(index, card)
        else:
            print("Error!")

    elif command == "Remove":
        if card in the_deck:
            the_deck.remove(card)
        else:
            print("Card not found.")

    elif command == "Swap":
        card_1_index = the_deck.index(card)
        card_2_index = the_deck.index(commands[2])
        the_deck[card_1_index], the_deck[card_2_index] = the_deck[card_2_index], the_deck[card_1_index]
    elif command == "Shuffle":
        the_deck.reverse()

    commands = input().split()

print(f"{' '.join(the_deck)}")