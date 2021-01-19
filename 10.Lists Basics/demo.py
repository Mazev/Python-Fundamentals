events = input().split('|')

energy = 100
coins = 0

for num in events:
    event_ingredient, number = num.split('-')
    number = int(number)

    if event_ingredient == 'rest':
        gain_energy = 0
        if energy + number <= 100:
            gain_energy = number
            energy += gain_energy
        else:
            gain_energy = 100 - energy
            print(f'You gained {gain_energy} energy.')
            print(f'Current energy: {energy}.')
    elif event_ingredient == 'order':
        energy -= 30
        if energy > 0:
            coins += number
            print(f"You earned {coins} coins.")
        if energy < 30:
            energy += 50
            print("You had to rest!")
    else:
        coins -= number
        if coins > 0:
            print(f'You bought {event_ingredient}.')
        else:
            print(f"Closed! Cannot afford {event_ingredient}.")

if coins > 0 and energy > 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
