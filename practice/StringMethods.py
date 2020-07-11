course = 'Python for beginners'

#length
print(len(course))
print(course.upper())
print(course.lower())

#title; her kelimenin ilk harfi uppera donusuyor
print(course.title())

#index bulmak icin
print(course.find('b'))

#olm adiginda -1 verir
print(course.find('F'))
print(course.find('y'))

#replace , harf ya da kelime fark etmez
print(course.replace('beginners','cool people'))

#ilk harfi buyuk yapiyor
print(course.capitalize())

#arraye donisturmek icin
print(course.split(' '))
print(course.split(' ', 1 ))
print(course.split())
words = course.split()
print(words)

#contains tru false doner ve case sensitive
print('python' in course)
print('Python' in course)

greet = 'Welcome to Ptyhon class 2020'
print('2020' in greet)
contains = 'Java' in greet
print(contains)
language = 'Java'
print(language in greet)
