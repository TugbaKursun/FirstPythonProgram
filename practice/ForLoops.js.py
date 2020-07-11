arr = ['Ayse', 'Tugba', 'Aysegul', 'Husniye', 'Leyla']
for item in arr:
    print(item)
# 5 kez yazdir
for item in range(5):
    print('Hello world!')

# 1 den 10 kadar yazdir
for number in range(1, 10):
    print(number)
# even numberlari yazdir
for even in range(0, 10, 2):
    print(even)

# examples

# reverse
reverse = ""
word = 'Python'
for ch in range(len(word), 0, -1):
    reverse += word[ch - 1]
print(reverse)

# find the sum of all odd numbers between 0 to 1000:

total = 0
for num in range(0, 1000):
    if num % 2 != 0:
        total += num

print(total)

# Ask user to enter 5 numbers
# Find the maximum number
numbers = []
i = 0
while i < 5:
 numbers.append(input('Enter a number: '))
 i += 1

maximum = int(numbers[0])
for j in numbers:
  if int(j) > int(maximum):
    maximum = j

print(f'Maximum number is : {maximum}')

arr_num = [5, 7, 66, 23, 76, 106, 654]

for num in arr_num:
    if num > 100:
        arr_num.remove(num)
print(arr_num)






