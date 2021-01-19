# moe reshenie
elektrons = int(input())

atom = []
elektron_counter = elektrons
for i in range(1, elektrons + 1):
    posible_elektrons = 2 * (i ** 2)
    if posible_elektrons > elektron_counter:
        atom.append(elektron_counter)
    else:
        atom.append(posible_elektrons)
    elektron_counter -= posible_elektrons
    if sum(atom) == elektrons:
        break

print(atom)

# reshenie na daskala
# number_elektrons = int(input())
#
# atom = []
# cell_number = 1
# while number_elektrons > 0:
#     posible_elektrons = 2 * cell_number ** 2
#     if posible_elektrons > number_elektrons:
#         atom.append(number_elektrons)
#     else:
#         atom.append(posible_elektrons)
#     number_elektrons -= posible_elektrons
#     cell_number += 1
# print(atom)


