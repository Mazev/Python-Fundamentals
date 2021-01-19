data = input().split()

products = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = int(data[i + 1])
    products[key] = value

products_in_sarch = input().split()

for el in products_in_sarch:
    if el in products:
        print(f"We have {products[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")
