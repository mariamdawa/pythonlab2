class Person:
    
    def validateHealthRate(self,healthRate):
        if not (healthRate>0 and healthRate<100):
            raise Exception()

    def __init__(self,full_name,money,sleepMood,healthRate):
        try:
            self.validateHealthRate(healthRate)
            self.full_name=full_name
            self.money=money
            self.sleepMood=sleepMood   
            self.healthRate=healthRate
        except:
            print("Invalid healthrate must be between 0 and 100")


    def sleep(self,hours):
        if hours==7:
            self.sleepMood="happy"
        elif hours<7:
            self.sleepMood="tired"
        elif hours>7:
            self.sleepMood="lazy"

    def eat(self,meals):
        if meals==3:
            self.healthRate+=100
        elif meals==2:
            self.healthRate+=75
        elif meals==1:
            self.healthRate+=50
    def buy(self,items):
        if items==1:
            self.money-=10
    
    