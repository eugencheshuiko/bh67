# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами

name = input('Enter your name: ')
age = input('Enter your ages: ')
city = input('Enter your city: ')

print('1. My name is ' + name + '. I\'m ' + age + ' y.o. I\'m from ' + city + '.')

print('2. My name is %s. I\'m %s y.o. I\'m from %s.' %(name, age, city))

print(f'3. My name is {name}. I\'m {age} y.o. I\'m from {city}.')

print('4. My name is {}. I\'m {} y.o. I\'m from {}.'.format(name, age, city))