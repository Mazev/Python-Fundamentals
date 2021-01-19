# # num_rooms = int(input())
# # cnt_free_chairs = 0
# # chairs = str
# # people = str
# #
# # for i in range(1, num_rooms + 1):
# #     chairs, people = input().split()
# #     people = int(people)
# #
# #     if len(chairs) < people:
# #         print(f"{people - len(chairs)} more chairs needed in room {i}")
# #
# #     else:
# #         free_chairs = len(chairs) - people
# #         cnt_free_chairs += free_chairs
# #
# # if not len(chairs) < people:
# #     print(f"Game On, {cnt_free_chairs} free chairs left")
#
#
#
# input_data = input().split()
# result = []
#
# for el in input_data:
#     str_to_convert = ''
#     str_result = []
#     for i in range(len(el)):
#         if el[i] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
#             str_to_convert += el[i]
#         else:
#             str_result.append(el[i])
#     str_to_convert = chr(int(str_to_convert))
#     str_result[0], str_result[len(str_result) - 1] = str_result[len(str_result) - 1], str_result[0]
#     str_result = str_to_convert + ''.join(str_result)
#     result.append(str_result)
#
# result = ' '.join(result)
# print(result)

kvartal = [int(i) for i in input().split("@")]
command = input()
old_index = 0
failed = 0

while not command == "Love!":
    place = int(command.split()[1])
    if not place + old_index > len(kvartal):
        place += old_index
    if not place > len(kvartal) - 1:
        if kvartal[place] < 0:
            print(f"Place {place} already had Valentine's day.")
        if not kvartal[place] <= 0:
            kvartal[place] -= 2
            if kvartal[place] == 0:
                print(f"Place {place} has Valentine's day.")
    else:
        kvartal[0] -= 2
        if kvartal[0] == 0:
            print(f"Place {0} has Valentine's day.")
        if kvartal[0] <= 0:
            print(f"Place {0} already had Valentine's day.")
    old_index += place
    command = input()
print(f"Cupid's last position was {place}.")

for el in kvartal:
    if el > 0:
        failed += 1

if failed > 0:
    print(f"Cupid has failed {failed} places.")
else:
    print("Mission was successful.")
