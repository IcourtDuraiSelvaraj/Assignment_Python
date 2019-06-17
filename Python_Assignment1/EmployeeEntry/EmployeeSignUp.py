import EmployeeEntry.EmployeeDetail
class Employee_SignUp:
    def employee_SignUp(self):
        try:
            employee_Name=input("Enter Name")
            age=input("Enter Age")
            designation = input("Enter Designation")
            experience=input("Enter Experience")
            password=input("Set Password")
            EmployeeEntry.EmployeeDetail.Employee_Detail().upload_Data(employee_Name, age, designation, experience, password)
        except NameError:
            print("Done")