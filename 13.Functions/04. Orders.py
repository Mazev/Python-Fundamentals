products = input()
quantity = int(input())


def praice(product, quantity):
    if products == 'coffee':
        return quantity * 1.50
    elif products == 'water':
        return quantity * 1.00
    elif products == 'coke':
        return quantity * 1.40
    elif products == 'snacks':
        return quantity * 2.00


print(f'{praice(products, quantity):.2f}')
