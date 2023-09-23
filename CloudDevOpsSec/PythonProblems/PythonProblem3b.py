from PythonProblem3a import *

check = True

while check:
    Name = input("Enter Employee's Name:\n")
    Id = input("Enter Employee's Id?\n")

    try:
        Type = get_employee_type()
    except ValueError as error:
        input_range = f"[1,{len(EmployeeType)}]"
        print(f"Invalid selection. Enter a value in range {input_range} \n")
        continue

    SalesMade = float(input("Enter the amount in Sales Employee made?\n"))

    e1 = Sales(Name,Id,Type,SalesMade)

    print(f"\nSalary of Employee {e1.EmployeeName}[{e1.EmployeeId}] Type '{Type.name}' is {e1.get_salary()}\n\nPlease Note!!! As Per Company Policy, {(EmployeeType._member_names_)[0]} gets 5% of Commission from the sales they made & {(EmployeeType._member_names_)[1]} get Base_Salary plus 5% of Commission from the sales they made\n")

    check = continue_check()