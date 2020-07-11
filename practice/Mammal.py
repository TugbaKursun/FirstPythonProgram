class Mammal:
 def walk(self):
print("walk")


class Dog(Mammal):
 def bark(self):
print("bark")


class Cat(Mammal):
 def be_annoying(self):
print("annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.walk()
cat1.be_annoying()
from practice.Employee import Employee
from practice.Department import Department

myDepartment = Department("IT", "Ayse Turk", "John Smith", 120000, "Mary Dillon", 15)
print("Employee name: " + myDepartment.name + " and his salary is " + str(myDepartment.salary))
print("Department manager: " + myDepartment.dept_manager)
myDepartment.department_meeting()
print("Monthly salary for " + myDepartment.name + "is " + str(myDepartment.monthly_salary()))


my_employee = Employee("Mary Dillon", 15, 200000, "Steve Jobs")
print(my_employee.name)
print("Monthly salary is : " + str(my_employee.monthly_salary()))