n = int(input())

ship_army = []
ship_destroyed = 0

for _ in range(n):
    ship = input().split()
    ships = list(map(int, ship))
    ship_army.append(ships)

attacks = input().split()

for el in attacks:
    attacks = el.split('-')

    row = int(attacks[0])
    col = int(attacks[1])

    if ship_army[row][col] < 1:
        continue

    elif ship_army[row][col] > 1:
        ship_army[row][col] -= 1

    elif ship_army[row][col] == 1:
        ship_army[row][col] -= 1
        ship_destroyed += 1

print(ship_destroyed)
