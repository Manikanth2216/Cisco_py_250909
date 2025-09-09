employees=[]
employee=('ironman',55,70000,True)
employees.append(employee)

employee=('spiderman',28,50000,True)
employees.append(employee)

employee=('captain america',105,50000,True)
employees.append(employee)

print('after add all employees:',employees)

I=0
search = 'spiderman'
index=-1
for emp in employees:
    if emp[0] == search:
        index=I
        break
    I+=1

if index==-1:
    print('Employee not found')
else:
    search_employee=employees[index]
    print(search_employee)
    salary=float(input('Salary:'))
    employee=(search_employee[0],search_employee[1],salary,search_employee[3])
    employees[index]=employee
print('after search and update:',employees)

employee=('thor',1005,50000,True)
employees.append(employee)
print('after addind thor:',employees)

position=1
employees.pop(position)
print('after deleting spiderman:',employees)