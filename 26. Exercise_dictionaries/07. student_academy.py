number = int(input())

students_data = {}

for _ in range(number):
    name = input()
    grades = float(input())
    if name not in students_data:
        students_data[name] = []
    students_data[name].append(grades)

filtred_students = {}

for name, grades in students_data.items():
    average_grades = sum(grades) / len(grades)
    if average_grades >= 4.50:
        filtred_students[name] = average_grades


for name, average_grades in sorted(filtred_students.items(), key=lambda x: x[1], reverse= True):
    print(f'{name} -> {average_grades:.2f}')

