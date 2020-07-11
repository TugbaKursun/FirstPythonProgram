count = 0
while count < 6:
    print('$' * count)
    count += 1
i = 6
while i>0:
    print('*' * i)
    i -= 1


# replace kullanirken replace("old", "new", max) max burada ne kadar
# replace edecegini belirtmek icin optioanl kullaniyorsun.
sentence = 'I like book, I read book'
bookCount = 0
while 'book' in sentence:
    sentence = sentence.replace('book', ' ',1)
    bookCount += 1
print(bookCount)

#100 e kadar olan cift sayilar
even = 1
while even <= 100:
    if even % 2 == 0:
        print(f' {even}')
    even += 1

#get 2 num and give nums of sum
answer = " "
while True:
    first_number = input('Enter first number: ')
    second_number = input('Enetr second number: ')
    add = int(first_number) + int(second_number)
    print(f'Addition is {add}')
    answer = input('Do you want to continue?')
    if answer.lower() == 'no':
        break
