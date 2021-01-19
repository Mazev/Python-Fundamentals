company = {}

data = input()
while not data == 'End':
    company_name, employeer = data.split(' -> ')
    if company_name not in company:
        company[company_name] = []
    if employeer not in company[company_name]:
        company[company_name].append(employeer)

    data = input()

for company_name, employeer in sorted(company.items(), key=lambda x: x[0]):
    print(company_name)
    for el in employeer:
        print(f'-- {el}')
