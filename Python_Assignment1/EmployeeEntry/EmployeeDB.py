import pickle

def upload_employee_record(employee_data):
    print(employee_data)
    print(employee_data['Name'])


    dbfile = open('Employee_DB', 'ab')
    #print("file open")

    pickle.dump(employee_data, dbfile)
    print("load into file")
    dbfile.close()
    print("successfully closed")
    loadData()


def loadData():
    #print("opening file")
    dbfile = open('Employee_DB', 'rb')
    db = pickle.load(dbfile)

    for keys in db:
       print(keys, '=>', db[keys])
    dbfile.close()


if __name__ == '__main__':
    db = {}

