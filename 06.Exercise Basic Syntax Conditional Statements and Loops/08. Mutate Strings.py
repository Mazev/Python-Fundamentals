first_string = input()
second_string = input()

current_string = ''
privious_string = first_string
for iteration in range(len(first_string)):
    for index_str_2 in range(0, iteration + 1):
        current_string += second_string[index_str_2]
    for index_str_1 in range(iteration + 1, len(first_string)):
        current_string += first_string[index_str_1]
    if not privious_string == current_string:
        print(current_string)
    privious_string = current_string
    current_string = ''
