operation = input()
num_1 = int(input())
num_2 = int(input())


def calculations(operations):
    if operation == 'multiply':
        return num_1 * num_2
    elif operation == 'divide':
        return num_1 // num_2
    elif operation == 'add':
        return num_1 + num_2
    elif operation == 'subtract':
        return num_1 - num_2


print(calculations(operation))
