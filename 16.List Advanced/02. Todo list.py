data = input()
todo_list = [0]*10

while data != "End":
    tokens = data.split('-')
    prioreti = int(tokens[0])
    note = tokens[1]
    todo_list.insert(prioreti, note)

    data = input()
result = [el for el in todo_list if el !=0]
# for el in todo_list:
#     if el != 0:
#         result.append(el)
print(result)


