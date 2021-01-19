event = input(). split('|')

energy = 100
coins = 100

for num in event:
    event_ingredient , number = num.split('-')
    number = int(number)

    if event_ingredient == 'rest':
        gained_energy = 0
        if energy + number <= 100:
            gained_energy = number
            energy += gained_energy
        else:
            gained_energy = 100 - energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif event_ingredient == 'order':
        energy -= 30
        if energy > 0:
            coins += number
            print(f"You earned {number} coins.")
        elif energy < 30:
            energy += 50
            print("You had to rest!")
            continue
    else:
        coins -= number
        if coins > 0:
            print(f"You bought {event_ingredient}.")
        else:
            print(f"Closed! Cannot afford {event_ingredient}.")
            break


if coins > 0 and energy > 0:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")