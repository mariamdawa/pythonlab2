#!/usr/bin/env python3
from Classes.employee import Employee
from  Classes.office import Office

print("Welcome to lab2\n")
option = ""
while option != "q":
    options_message="Enter New Employee \t add\n"+\
                    "Delete Employee \t delete\n"+\
                    "View All Employees \t all\n"+\
                    "View Employee By ID \t id\n"+\
                    "Quit \t\t\t q\n"
    option=input(options_message)
    if option == "add":
        adding_option=input("For Manager \t mngr\n"+\
                            "For Normal \t nrml\n")
        if adding_option == "mngr":
            is_manager="true"
        elif adding_option == "nrml":
            is_manager="false"
        else:
            raise Exception("Please enter a valid option next time!\n")
        name=input(">>Name: \n")
        id=input(">>ID: \n")
        email=input(">>Email: \n")
        salary=input(">>Salary: \n")
        employee=Employee(name,id,email,salary,is_manager)
        Office().hire(employee)

    elif option == "delete":
        id=input(">>ID: \n")
        Office().fire(id)

    elif option == "all":
        Office().get_all_employees()

    elif option == "id":
        id=input(">>ID: \n")
        Office().get_employee(id)
    elif option == "q":
        exit()
    else:
        print ("Enter a valid option")
