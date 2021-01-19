num_day = int(input())
count_players = int(input())
group_energy = float(input())
water_per_day_one_person = float(input())
food_per_day_one_person = float(input())

total_water = num_day * count_players * water_per_day_one_person
total_food = num_day * count_players * food_per_day_one_person
day_count = 0


for _ in range(num_day):
    energy_lost = float(input())
    day_count += 1
    group_energy -= energy_lost
    if group_energy <= 0:
        break
    if day_count % 2 == 0:
        group_energy += group_energy * 0.05
        total_water -= (total_water * 0.30)
    if day_count % 3 == 0:
        group_energy += group_energy * 0.10
        total_food -= (total_food / count_players)


if group_energy > 0:
    print(f'You are ready for the quest. You will be left with - {group_energy:.2f} energy!')
else:
    print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.')