import EmployeeEntry.EmployeeSignIn
import EmployeeEntry.EmployeeSignUp

def employee_Entry_Check():
    try:
        print("Press 1 or 2")
        print("1.SignIn")
        print("2.SignUp")
        decision = 0
        decision = int(input("Enter your decision"))
        if decision == 1:
            print("Employee SignIn")
            EmployeeEntry.EmployeeSignIn.Employee_SignIn().employee_SignIn()
        elif decision == 2:
            print("Employee SignUp")
            EmployeeEntry.EmployeeSignUp.Employee_SignUp().employee_SignUp()
        else:
            print("Enter proper decision")
            employee_Entry_Check()
    except ValueError:
        print("Enter your choice")
        employee_Entry_Check()
    finally:
        pass
employee_Entry_Check()
