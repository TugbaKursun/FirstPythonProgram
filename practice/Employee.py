class Employee:
def __init__(self, name, department_id, salary, manager):
self.name = name
self.department_id = department_id
self.salary = salary
self.manager = manager

def info(self):
print("Employee name: " + self.name + "\nDepartment id: " + str(self.department_id) +
"\nEmployee salary: " + str(self.salary) + "\nEmployee's manager: " + self.manager)

def monthly_salary(self):
return float(self.salary / 12)
from practice.Employee import Employee
emp1 = Employee("Ayse", 12, 150000, "John Smith")

print(emp1.name)
emp2 = Employee("Husniye", 12, 160000, "Mary Smith")
emp2.info()

print("Monthly salary for " + emp2.name + " is " + str(emp2.monthly_salary()))
print("Monthly salary for " + emp1.name + " is " + str(emp1.monthly_salary()))
def cube(num):
return num * num * num


print(cube(9))


def remove_duplicates(string):
non_dup = ""
for ch in string:
if ch not in non_dup:
non_dup += ch
return non_dup


print(remove_duplicates("AAABBCCDEFG"))


def display():
print("Welcome to Python class")


display()
five_cube = cube(5)
print(five_cube)


def info(first_name, last_name):
print(f"Hello {first_name} {last_name} , Welcome to our Python class-101")


info("Ayse", last_name="Turk")
info("Husniye", "Imamoglu")
info(first_name="Tugba", last_name="Kursun")
try:
number = int(input("Enter a number: "))
print(number)
except ValueError:
print("Invalid Input")


try:
value = 10/0
except ZeroDivisionError as err:
print(err)
