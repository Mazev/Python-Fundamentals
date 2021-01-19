password = input()


def pasword_valodator(password):
    is_valide = True
    counter_numbers = 0
    if not (6 <= len(password) <= 10):
        is_valide = False
        print("Password must be between 6 and 10 characters")
    for el in password:
        if not el.isdigit() and not el.isalpha():
            is_valide = False
            print("Password must consist only of letters and digits")
            break
        if el.isdigit():
            counter_numbers += 1
    if counter_numbers < 2:
        is_valide = False
        print("Password must have at least 2 digits")

    return is_valide


result = pasword_valodator(password)
if result:
    print("Password is valid")
