is_real = True
if is_real:
    print("It's real, you can get everything free!")
else:
    print("Wake up! It is a dream!")

number = 5
if number > 2:
    print('You almost there, keep working hard')

# if statements
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
    print("Enjoy your day")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")


has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
# comparison operators

temperature = 30

if temperature > 30:
    print("it's a hot day")
else:
    print("it's not a hot day")

name = "Jack"

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

#ornek
grade = 90
grade = 100
if grade <= 100:
    if 90 <= grade <= 100:
        print("Your grade is A")
    elif 80 <= grade < 90:
        print("Your grade is B")
    elif 70 <= grade < 80:
        print("Your grade is C")
    elif 60 <= grade < 70:
        print("Your grade is D")
    else:
        print("Your grade is F")
else:
    print("Invalid grade!")