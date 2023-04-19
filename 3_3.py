# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
# 1
name = input()
age = input()
city = input()




print('hi' + name + 'age' + age)
# print('hi %s age %d sity' % (name, age)
print(f'hi {name} age {age}')
print('hi {} age {}'.format(name, age))

