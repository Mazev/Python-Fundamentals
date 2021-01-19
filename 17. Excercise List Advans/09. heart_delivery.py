neighborhood = list(map(int, input().split('@')))

curent_house = 0
jump_cmd = input().split()
while not jump_cmd == 'Love!':
    lenght_jump = int(jump_cmd[1])
    if curent_house + int(lenght_jump) > len(neighborhood) - 1:
        curent_house = 0
    else:
        curent_house += lenght_jump
    if not neighborhood[curent_house] == 0:
        neighborhood[curent_house] -= 2
        if neighborhood[curent_house] == 0:
            print(f"Place {curent_house} has Valentine's day.")
    else:
        print(f"Place {curent_house} already had Valentine's day.")

    jump_cmd = input().split()

print(f"Cupid's last position was {curent_house}.")
fail = 0
for el in neighborhood:
    if el == 0:
        fail += 1
if fail > 0:
    print(f"Cupid has failed {fail} places.")
else:
    print("Mission was successful.")


# def jumping_in_neighborhood(neighborhood):
#     crnt_house = 0
#     jump_cmd = input().split()
#     while not jump_cmd[0] == "Love!":
#         length_jump = int(jump_cmd[1])
#         if crnt_house + int(length_jump) > len(neighborhood) - 1:
#             crnt_house = 0
#         else:
#             crnt_house += length_jump
#         if not neighborhood[crnt_house] == 0:
#             neighborhood[crnt_house] -= 2
#             if neighborhood[crnt_house] == 0:
#                 print(f"Place {crnt_house} has Valentine's day.")
#         else:
#             print(f"Place {crnt_house} already had Valentine's day.")
#
#         jump_cmd = input().split()
#
#     return [[i for i in neighborhood if not i == 0], crnt_house]
#
#
# neighborhood = input().split("@")
# neighborhood = list(map(int, neighborhood))
#
# failed, house_stopped = jumping_in_neighborhood(neighborhood)
# print(f"Cupid's last position was {house_stopped}.")
# if not failed:
#     print("Mission was successful.")
# else:
#     print(f"Cupid has failed {len(failed)} places.")