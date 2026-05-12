#payroll program
class Employee:
    def __init__(self,name,base_money):
        self.name = name
        self.base_money = base_money

class FullTime(Employee):
    def __init__(self,name,base_money,OT_hour):
        super().__init__(name,base_money)
        self.OT_hour = OT_hour
    def calculate_pay(self):
        OT = 15 * self.OT_hour
        salary = self.base_money + OT
        return salary

class PartTime(Employee):
    def __init__(self, name, base_money, work_hour):
        super().__init__(name, base_money)
        self.work_hour = work_hour
    def calculate_pay(self):
        salary = self.base_money * self.work_hour
        return salary

class Freelancer(Employee):
    def __init__(self, name, num_project):
        super().__init__(name,num_project)
        self.num_project = num_project
    def calculate_pay(self):
        salary = 250 * self.num_project
        return salary

employees =[FullTime("Ali",1700,8),
PartTime("Kuma",8,128),
Freelancer("Stella",10)]

for emp in employees:
    print(emp.calculate_pay())