#Task-Given the list of the employees age, salary and name, display the employees name and age,
# the maximum salary of the employee and the average salary.

def employee_details(employee_salary,emp_list,age):
    dict={}
    for i in range(len(emp_list)):
        dict[emp_list[i]]=age[i]
    sal=[]
    for i in employee_salary:
        for s in i.values():
            sal.append(s)
    print("Employee and their ages ",dict)
    print("Maximum salary is ",max(sal))
    print("Average salary is ", round(sum(sal)/len(sal)))

salary=[{"Sam":230004},{"Priya":345009},{"Val":456778}]
employee=["Val","Sam","Priya"]
ages=["34","12","17"]
employee_details(salary,employee,ages)
