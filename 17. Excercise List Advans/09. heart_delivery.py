neighborhood = list(map(int, input().split('@')))

curent_hous = 0
data = input()
while not data == 'Love!':
    asd = data.split()
    lenght_jumps = int(asd[1])
    if curent_hous + int(lenght_jumps) > len(neighborhood) - 1:
        curent_hous = 0
    else:
        curent_hous += lenght_jumps

    if not neighborhood[curent_hous] == 0:
        neighborhood[curent_hous] -= 2
        if neighborhood[curent_hous] == 0:
            print(f"Place {curent_hous} has Valentine's day.")
    else:
        print(f"Place {curent_hous} already had Valentine's day.")

    data = input()

print(f"Cupid's last position was {curent_hous}.")
fail = 0
for el in neighborhood:
    if el > 0:
        fail += 1

if fail == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {fail} places.")
