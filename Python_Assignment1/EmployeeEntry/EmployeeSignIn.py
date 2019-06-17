import EmployeeEntry.EmployeeAvailability
class Employee_SignIn:
    def employee_SignIn(self):
        try:
            employee_Name=input("Enter Employee Name")
            password=input("Enter Password")
            EmployeeEntry.EmployeeAvailability.employee_Availability(employee_Name, password)

        except:
            pass

