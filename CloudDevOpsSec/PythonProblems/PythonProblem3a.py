class Employee:
    BaseSalary = 100

    def __init__(self,Name,Id,Type):
        self.EmployeeName = Name
        self.EmployeeId = Id
        self.EmployeeType = Type

def percent(SalesMade):
    Percent = float((5*SalesMade)/100)
    return Percent

class Sales(Employee):
    def __init__(self,Name,Id,Type,Sales):
        super().__init__(Name,Id,Type)
        self.SalesMade = float(Sales)
        self.Percentage_Sales_Made = float(percent(self.SalesMade))
        
    def get_salary(self):
        if Type == "CommissionEmployee":
            self.Salary = float(self.Percentage_Sales_Made)
        else:
            self.Salary = float(self.Percentage_Sales_Made) + float(Employee.BaseSalary)
        
        return self.Salary

Name = input("Enter you Name:\n")
Id = input("Enter your Employee Id?\n")
Type_Response = input("Are you a CommissionEmployee(yes\\no)?\n")

if Type_Response == "yes":
    Type = "CommissionEmployee"
else:
    Type = "SalariedCommissionEmployee"

SalesMade = float(input("Enter the amount in sales you made?\n"))

e1 = Sales(Name,Id,Type,SalesMade)

print(f"Your Salary is {e1.get_salary()}")