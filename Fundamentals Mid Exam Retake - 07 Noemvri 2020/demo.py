orders_the_shop = int(input())
price_for_capsule = float(input())
days = int(input())
capsules_count = int(input())
total = 0
price_coffee = 0

while orders_the_shop >0:
    price_for_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    price_coffee += ((days * capsules_count) * price_for_capsule)
    total +=((days * capsules_count) * price_for_capsule)

print(f'The price for the coffee is: ${price_coffee:.2f}')
print(f"Total: ${total:.2f}")