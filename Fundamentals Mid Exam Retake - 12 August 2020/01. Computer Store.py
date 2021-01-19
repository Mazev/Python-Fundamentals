price_without_taxes = 0
taxes = 0
total = 0
while True:
    command_and_praice = input()

    if command_and_praice == 'special':
        if total <= 0:
            print("Invalid order!")
            break
        else:
            total -= total * 0.10
            print("Congratulations you've just bought a new computer!")
            print(f'Price without taxes: {price_without_taxes:.2f}$')
            print(f'Taxes: {taxes:.2f}$')
            print("-----------")
            print(f'Total price: {total:.2f}$')
            break
    elif command_and_praice == 'regular':
        if total <= 0:
            print("Invalid order!")
            break
        else:
            print("Congratulations you've just bought a new computer!")
            print(f'Price without taxes: {price_without_taxes:.2f}$')
            print(f'Taxes: {taxes:.2f}$')
            print("-----------")
            print(f'Total price: {total:.2f}$')
            break
    money = float(command_and_praice)
    if money < 0:
        print("Invalid price!")
        continue
    price_without_taxes += money
    taxes += money * 0.20
    total = price_without_taxes + taxes
