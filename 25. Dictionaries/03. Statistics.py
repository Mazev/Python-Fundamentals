product_data = input()

products_dict = {}
while not product_data == 'statistics':
    product, quantity = product_data.split(': ')
    quantity = int(quantity)
    if product in products_dict:
        products_dict[product] += quantity
    else:
        products_dict[product] = quantity

    product_data = input()

print("Products in stock:")
for key, value in products_dict.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(products_dict)}')
print(f'Total Quantity: {sum(products_dict.values())}')