from Database.db import Db

class Office:

    def get_all_employees(self):
        employees = Db().get_all_employees()
        for employee in employees:
            print("\n\nName: "+str(employee[0])+\
                 "\nID: "+str(employee[1])+\
                "\nEmail: "+str(employee[2])+\
                "\nSalary: "+str(employee[3])+\
                "\nManager: "+str(employee[4]+"\n"))

    def get_employee(self, id):
        employee = Db().get_employee(id)
        print("\n\nName: "+str(employee[0][0])+\
              "\nID: "+str(employee[0][1])+\
                "\nEmail: "+str(employee[0][2])+\
                "\nSalary: "+str(employee[0][3])+\
                "\nManager: "+str(employee[0][4]+"\n"))

    def hire(self,employee):
        Db().insert_employee(employee)
        print("Employee hired successfully!")

    def fire(self,id):
        Db().delete_employee(id)
        print("Employee Fired successfully!")


