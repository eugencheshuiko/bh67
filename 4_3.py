# *Заполнить словарь где ключами будут выступать числа от 0 до n, а значениями вложенный словарь с ключами "name" и "email", а значения для этих ключей будут браться с клавиатуры.
n = int(input('Enter n: '))
data = {i + 1: {'name': input(f'name {i + 1}: '), 'email': input(f'email {i + 1}: ')} for i in range(n)}
print(data)
