n  = int(input())

softuni_parking = {}

for _ in range(n):
    token = input().split()
    commands = token[0]
    if commands == 'register':
        username = token[1]
        plate_number = token[2]
        if not username in softuni_parking:
            softuni_parking[username] = plate_number
            print(f'{username} registered {plate_number} successfully')
        else:
            print(f'ERROR: already registered with plate number {plate_number}')
    if commands == 'unregister':
        username = token[1]
        if username in softuni_parking:
            print(f"{username} unregistered successfully")
            softuni_parking.pop(username)
        else:
            username = token[1]
            print(f"ERROR: user {username} not found")


for username, plate_number in softuni_parking.items():
    print(f"{username} => {plate_number}")

# print(f"{username} => {plate_number}")

