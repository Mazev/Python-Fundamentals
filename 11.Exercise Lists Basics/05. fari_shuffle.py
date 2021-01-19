cards = input().split()
shuffles_count = int(input())
half = len(cards) // 2

for i in range(shuffles_count):
    rez = []
    for index in range(half):
        first_card = cards[index]

        current_index_second_deck = index + half
        second_card = cards[current_index_second_deck]

        rez.append(first_card)
        rez.append(second_card)
    cards = rez

print(rez)
