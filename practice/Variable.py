#comment yazabilriz

print('Tugba')
print("Kursun")
# 10 tane @ yazdirir
print('@' * 10)
#alat alta yazdirmak isterseniz

name = "Tugba"
#Booleanlarda True / False
is_true = True
is_apple = False
price = 10
age = 20
rating = 4.9
print(price)
pi = 3.14
print(pi)

#Scanner , userin cevabini variable olrak store ediyoruz like dinner
#tekrar dinner oilarak yazdigimizda userin cevabini yazdiracak

dinner=input('What did you cook today?')
print('I cooked ' + dinner )


## ''' ciktilari farkli linelarda yazabilmek icin.
# hangi satiri altta yazdirmak istiyiorsak manually alt satira koyariz

print('''Welcome to Python class 
Python is fun''')

#stringi concat ediyorsak baska bir typ ile
#print(f"Net salary is :  {net_salary}") --> format edip {}
# kullaniyoruz typeni  belirtmeye gerek kalmayacak + da gerek kalmayacak
#inputkar her zaman string olarak gelir typi degistirmek icin casting yapammaiz gerekir
salary= input("Employee salary: ")
print("Employee salary is  " + salary)
insurance= input("Insurance : ")
net_salary = int(salary) - int(insurance)
print(f"Net salary is :  {net_salary}")


#print with "string"
print(""" "yields the empty string" """)
