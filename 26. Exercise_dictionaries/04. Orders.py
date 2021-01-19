products_price = {}
products_quantities = {}

data = input()

while not data == 'buy':
    products, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    if products not in products_price:
        products_price[products] = price
        products_quantities[products] = quantity
    else:
        products_price[products] = price
        products_quantities[products] += quantity

    data = input()

for products, price in products_price.items():
    total_price = price * products_quantities[products]
    print(f'{products} -> {total_price:.2f}')
