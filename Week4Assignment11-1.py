# Author: Dalton Cone 
# Purpose: Write two classes, Employee and ProductionWorker. Get input for the attributes and display them. 
# Name: Week3Assignment11-4.py

class Employee:

    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number

    # Accessor methods
    def getName(self):
        return self.name
    
    def getEmployeeNumber(self):
        return self.employee_number

    # Mutator methods
    def setName(self, name):
        self.name = name

    def setEmployeeNumber(self, employee_number):
        self.employee_number = employee_number

    def __str__(self):
        return "Employee Name: " + self.getName() + ", Employee Number: " + str(self.getEmployeeNumber())
    
class ProductionWorker(Employee):

    def __init__(self, name, employee_number, shift_number, hourly_pay_rate):
        Employee.__init__(self, name, employee_number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

    # Accessor methods
    def getShiftNumber(self):
        return self.shift_number

    def getHourlyPayRate(self):
        return self.hourly_pay_rate

    def __str__(self):
        return "\nWorker Name: " + self.getName() + " \nWorker Number: " + str(self.getEmployeeNumber()) + \
               " \nWorker Shift Number: " + str(self.getShiftNumber()) + \
               " \nWorker Hourly Pay Rate: " + str(self.getHourlyPayRate())

worker_name = input("Please Enter the worker name: ")
worker_number = int(input("Please Enter the worker number: "))
worker_shift_number = int(input("Please Enter the worker shift number: "))
worker_hourly_pay_rate = float(input("Please Enter the worker hourly pay rate: "))
worker = ProductionWorker(worker_name, worker_number, worker_shift_number, worker_hourly_pay_rate)

print(worker.__str__())
     