import EmployeeEntry.EmployeeDB
class Employee_Detail:
    def upload_Data(self, employee_name, age, designation, experience, password):
        try:
            self.employee_name=employee_name
            self.age=age
            self.designation=designation
            self.experience=experience
            self.password=password
            #print(self.employee_name,self.age,self.designation)

            employee_Data={}
            employee_Data['Name'] = self.employee_name
            employee_Data['Age'] = self.age
            employee_Data['Designation'] = self.designation
            employee_Data['Experience'] = self.experience
            employee_Data['Password'] = self.password
            #print("Dictionary page")
            #uploadData['Employee_Name'] = upload_Data
            #print(employee_Data)

            EmployeeEntry.EmployeeDB.upload_employee_record(employee_Data)
        except ValueError:
            print("Error")



