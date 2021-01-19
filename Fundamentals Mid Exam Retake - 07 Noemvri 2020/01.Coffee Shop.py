orderPrice = 0
total = 0
orders_the_shop = int(input())
while orders_the_shop == orders_the_shop:
    price_for_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    orderPrice = ((days * capsules_count) * price_for_capsule)
    orders_the_shop -= 1
    total += orderPrice
    print(f'The price for the coffee is: ${orderPrice:.2f}')
print(f"Total: ${total:.2f}")
