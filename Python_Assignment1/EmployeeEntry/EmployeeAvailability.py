import pickle

def employee_Availability(name, password):
    print(name+" "+password)
    dbfile = open('Employee_DB', 'rb')
    data = pickle.load(dbfile)
    #print(data['Name'])
     if data['Name'] in name and data['Password'] in password:
        print("Success")
    dbfile.close()
