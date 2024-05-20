# Encapsulation principle: Attributes and behaviour/ method are bundled together with class
# Defining common class and attributes
class Person:
    def __init__(self, name, age, cid, salary, children, nppf, employee_type, Organization_type="Government"):
        self.name = name
        self.age = age
        self.cid = cid
        self.salary = salary 
        self.children = children
        self.nppf = nppf
        self.employee_type = employee_type
        self.Organization_type = Organization_type
        self.income = salary  # Assuming income is derived from salary and assumed as annual income
     
     # Common behaviour
        def walk(self):
            print(self.name, "is walking")
        def talk(self):
            print(self.name, "is talking")    
        def sleep(self):
            print(self.name, "is sleeping")
        def eat(self):
            print(self.name, "is eating") 
        def earn(self):
            print(self.name, "is earning") 


    def calculate_tax(self):
        income = self.income
        deductions = 0

        # Deductions for children
        children_deduction = self.get_child_deduction()
        deductions += children_deduction

        # Additional deductions based on employee and organization types
        if self.employee_type == "Contract" and self.Organization_type!= "Government":
            deductions += self.get_nppf_deduction()
        elif self.employee_type == "Regular" and self.Organization_type == "Government":
            deductions += self.get_nppf_deduction()

        # Tax calculation based on taxable income and deductions
        if income <= 300000:
            return 0
        elif income < 400000:
            return income * 0.10
        elif income <= 650000:
            return income * 0.15
        elif income <= 1000000:
            return income * 0.20
        elif income <= 1500000:
            return income * 0.25
        else:
            return income * 0.30

    def get_child_deduction(self):
        if self.children > 0:
            return self.children * 350000  # deduction
        else:
            return 0

    def get_nppf_deduction(self):
        if self.employee_type == "Contract" and self.Organization_type!= "Government":
            return self.salary * 0.05  #  deduction
        else:
            return 0

# Inheritance principle
class Nurse(Person): # # Nurse is inheriting from person
    def __init__(self, name, age, cid, salary, children, nppf, employee_type, Organization_type, department, shift):
        super().__init__(name, age, cid, salary, children, nppf, employee_type, Organization_type)
        self.department = department
        self.shift = shift

# Behaviour/ method
    def care(self):
        print(self.name, "is caring patients")

    def educating(self):
        print(self.name, "is educating patients and their families on treatment plans and self care")

 # Accountant is inheriting from person
class Accountant(Person):
    def __init__(self, name, age, cid, salary, children, nppf, employee_type, Organization_type, designation):
        super().__init__(name, age, cid, salary, children, nppf, employee_type, Organization_type)
        self.designation = designation

# Behaviour/ method
    def managing(self):
        print(self.name, "is managing financial records and transactions")

    def preparing(self):
        print(self.name, "is preparing financial statements")

# Creating objects/instances for different classes
nurse1 = Nurse("Sangay", 26, 10705002435, 400000, 1, 6000, "Regular", "Government", "Emergency room", "Night")
nurse2= Nurse("Deki",32,10704560098,450000,2, 0, "Contract","Government","Medical_surgical","Day") 
accountant1 = Accountant("Dema", 37, 10705009614, 605000, 3, 0, "Contract", "Government", "Certified Internal Auditor")
accountant2= Accountant("Phuntsho",27,10705008756,510000,0,12000,"Rugular","Government","Certified Public Accountant")


# Polymorphic principle(common interface for calculating tax)
for person in [nurse1, nurse2, accountant1, accountant2]:
    print(f"{person.name}'s tax is {person.calculate_tax()}")


# Reference
# Acts & Policy | Ministry of Finance, Royal Government of Bhutan. (n.d.). https://www.mof.gov.bt/publications/acts-policy/
# What is PIT? | Department of Revenue & Customs:Ministry of Finance. (n.d.). http://portal.drc.gov.bt/drc/node/25
# freeCodeCamp.org. (2021, October 13). Object Oriented Programming with Python - Full Course for Beginners [Video]. YouTube. https://www.youtube.com/watch?v=Ej_02ICOIgs