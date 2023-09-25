from enum import IntEnum

class Employee:
    BaseSalary = float(1000)

    def __init__(self,Name,Id,Type,SalesMade):
        self.EmployeeName = Name
        self.EmployeeId = Id
        self.EmployeeType = Type
        self.SalesMade = SalesMade

class EmployeeType(IntEnum):
    CommissionEmployee = 1
    SalariedCommissionEmployee = 2

class CommissionEmployee(Employee):
    def __init__(self,Name,Id,Type,SalesMade):
        super().__init__(Name,Id,Type,SalesMade)
    
    def salary(self):
        return float(percent(self.SalesMade))
    
class SalariedCommissionEmployee(CommissionEmployee):
    def __init__(self,Name,Id,Type,SalesMade):
        super().__init__(Name,Id,Type,SalesMade)

    def salary(self):
        return super().salary() + float(Employee.BaseSalary)
   
def percent(SalesMade):
    Percent = float((5*SalesMade)/100)
    return Percent

def get_employee_type():
    Type_response = input(f"Enter the Employee Type? Enter '{EmployeeType.CommissionEmployee}' for {(EmployeeType._member_names_)[0]} or '{EmployeeType.SalariedCommissionEmployee}' for {(EmployeeType._member_names_)[1]}: ")
    Type = EmployeeType(int(Type_response))
    return Type

def continue_check():
    resp = input("Would you like to check salary for a different employee? (yes/no): ")
    if resp != "yes":
        print(f"\nExiting Now!!!\n")
        return False