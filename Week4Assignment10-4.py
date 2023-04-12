# Author: Dalton Cone 
# Purpose: Write a class named Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.
# Name: Week3Assignment10-4.py

class Employee:

    def __init__(self, name, id, department, title):
        self.name = name
        self.id = id
        self.department = department
        self.title = title

    def __str__(self):
        return '\nName: {self.name} \nID: {self.id} \nDepartment: {self.department} \nTitle: {self.title}'.format(self=self)

def main():
    e1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
    e2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
    e3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')
    print(e1)
    print(e2)
    print(e3)


main()
