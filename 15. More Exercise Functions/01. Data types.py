command_1 = input()
command_2 = input()


def data_types(type_1, type_2):
    if type_1 == 'int':
        type_2 = int(type_2)
        print(type_2 * 2)
    elif type_1 == 'real':
        type_2 = float(type_2)
        print(f'{(type_2 * 1.5):.2f}')
    else:
        print(f'${type_2}$')


data_types(command_1, command_2)
