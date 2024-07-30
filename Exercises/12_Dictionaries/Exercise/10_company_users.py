company_db = {}

command = input()
while command != "End":
    company_name, employee = command.split(" -> ")
    if company_name not in company_db:
        company_db[company_name] = []
    if employee not in company_db[company_name]:
        company_db[company_name].append(employee)
    command = input()

for company_name, employees in company_db.items():
    print(f"{company_name}")
    for employee_id in employees:
        print(f"-- {employee_id}")
