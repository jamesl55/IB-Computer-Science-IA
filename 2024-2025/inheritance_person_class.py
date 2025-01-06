class Person:
  def person_info(self, name, age):
    print("\nInside the Person Class there are:")
    print("Name:", name)
    print("Age:", age)

class Company:
  def company_info(self, company_name, location):
    print("Inside the Company Class there are:")
    print("Company Name:", company_name)
    print("Location:", location)

class Employee(Person, Company):
  def employee_info(self, salary, skill):
    print("Inside the Employee Class there are:")
    print("Salary:", salary)
    print("Skill:", skill)

name = input("Name: ")
age = int(input("Age: "))
company_name = input("Company Name: ")
location = input("Location: ")
salary = float(input("Salary: "))
skill = input("Skill: ")

Emp = Employee()

Emp.person_info(name, age)
Emp.company_info(company_name, location)
Emp.employee_info(salary, skill)