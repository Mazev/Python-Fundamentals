input_data = input().split()
result = []

for el in input_data:
    str_convert = ''
    str_result = []
    for i in range(len(el)):
        if el[i] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            str_convert += el[i]
        else:
            str_result.append(el[i])
    str_convert = chr(int(str_convert))
    str_result[0], str_result[len(str_result) - 1] = str_result[len(str_result) - 1],str_result[0]
    str_result = str_convert + ''.join(str_result)
    result.append(str_result)
print(*result)