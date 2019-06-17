import pickle

def employee_Availability(name, password):
    print(name+" "+password)
    dbfile = open('EmployeeDB', 'rb')
    data = pickle.load(dbfile)
    print(data['Name'])
    dbfile.close()