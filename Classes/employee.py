import re
from Classes.person import Person


class Employee(Person):
    workMood="nuetral"
    def __init__(self,full_name,id,email,salary,is_manager):
  
        self.validateEmail(email)
        self.validateSalary(salary)
        self.full_name=full_name
        self.id=id
        self.email=email
        self.salary=salary
        self.is_manager=is_manager
       
    def work(self,hours):
        if hours==8:
            self.workMood="happy"
        elif hours<8:
            self.workMood="lazy"
        elif hours>8:
            self.workMood="tired"
        

    def sendEmail(self,to,subject,body,reciever_name):
        f=open("emai.txt","w")
        emailFormat="To: "+to+\
                     "\nSubject: "+subject+\
                     "\nReciever Name: "+reciever_name+\
                     "\nFrom: "+self.email+\
                     "\n\nMessage: "+body
        f.write(emailFormat)
        f.close()
    
    def validateEmail(self,email):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if not re.search(regex, email):
            raise Exception("Invalid Email")
    
    def validateSalary(self,salary):
        if int(salary)<1000:
            raise Exception("Invalid Salary ")