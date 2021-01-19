fire_data = input().split('#')
water = int(input())

HIGH_FIRE = range(81, 126)
MEDIUM_FIRE = range(51, 81)
LOW_FIRE = range(1, 51)

effort = 0
put_of_fire = []
for fire in fire_data:
    type_of_fire, value = fire.split(' = ')
    value = int(value)

    if type_of_fire == 'High' and not value in HIGH_FIRE:
        continue
    elif type_of_fire == 'Medium' and not value in MEDIUM_FIRE:
        continue
    elif type_of_fire == 'Low' and not value in LOW_FIRE:
        continue
    if water >= value:
        water -= value
        effort += value * 0.25
        put_of_fire.append(value)
print('Cells:')
for fire_value in put_of_fire:
    print(f' - {fire_value}')

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_of_fire)}")

