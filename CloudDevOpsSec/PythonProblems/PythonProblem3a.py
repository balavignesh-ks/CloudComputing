from enum import IntEnum

class Employee:
    BaseSalary = float(1000)

    def __init__(self,Name,Id,Type):
        self.EmployeeName = Name
        self.EmployeeId = Id
        self.EmployeeType = Type

class EmployeeType(IntEnum):
    CommissionEmployee = 1
    SalariedCommissionEmployee = 2

class Sales(Employee):
    def __init__(self,Name,Id,Type,Sales):
        super().__init__(Name,Id,Type)
        self.SalesMade = float(Sales)
        self.Percentage_Sales_Made = float(percent(self.SalesMade))
        
    def get_salary(self):
        if  self.EmployeeType == EmployeeType.CommissionEmployee:
            self.Salary = float(self.Percentage_Sales_Made)
        else:
            self.Salary = float(self.Percentage_Sales_Made) + float(Employee.BaseSalary)
        
        return self.Salary
    
def percent(SalesMade):
    Percent = float((5*SalesMade)/100)
    return Percent

def get_employee_type():
    Type_response = input(f"Is the employee {(EmployeeType._member_names_)[0]} or {(EmployeeType._member_names_)[1]}? Enter '{EmployeeType.CommissionEmployee}' for {(EmployeeType._member_names_)[0]} or '{EmployeeType.SalariedCommissionEmployee}' for {(EmployeeType._member_names_)[1]}: ")
    Type = EmployeeType(int(Type_response))
    return Type

def continue_check():
    resp = input("Would you like to check salary for a different employee? (yes/no): ")
    if resp != "yes":
        print(f"\nExiting Now!!!\n")
        return False