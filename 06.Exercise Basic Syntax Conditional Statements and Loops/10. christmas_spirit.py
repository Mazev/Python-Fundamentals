quantity = int(input())
days = int(input())

chrismas_spirit = 0
total_money = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 10 == 0:
        chrismas_spirit -= 20
        total_money += tree_skirt_price + tree_garlands_price + tree_lights_price
        if day == days:
            chrismas_spirit -= 30
    if day % 2 == 0:
        total_money += ornament_set_price * quantity
        chrismas_spirit += 5
    if day % 3 == 0:
        total_money += tree_skirt_price * quantity + tree_garlands_price * quantity
        chrismas_spirit += 13
    if day % 5 == 0:
        total_money += tree_lights_price * quantity
        chrismas_spirit += 17
        if day % 3 == 0:
            chrismas_spirit += 30

print(f"Total cost: {total_money}")
print(f"Total spirit: {chrismas_spirit}")
