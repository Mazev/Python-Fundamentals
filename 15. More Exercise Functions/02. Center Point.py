x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())


def center_point(a, b, c, d):
    if (a + b) < (c + d):
        return c, d
    else:
        return a, b


center_point(x_1, y_1, x_2, y_2)

print(center_point(x_1, y_1, x_2, y_2))