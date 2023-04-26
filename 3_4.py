# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

num1 = float(input('Введите 1 число: '))
num2 = float(input('Введите 2 число: '))
num3 = float(input('Введите 3 число: '))
pos1 = num1 > 0 and num1 != 0
pos2 = num2 > 0 and num2 != 0
pos3 = num3 > 0 and num3 != 0
sum_pos = pos1 + pos2 + pos3
neg1 = num1 < 0 and num1 != 0
neg2 = num2 < 0 and num2 != 0
neg3 = num3 < 0 and num3 != 0
sum_neg = neg1 + neg2 + neg3
print('Положительных: ' + str(sum_pos))
print('Отрицательных: ' + str(sum_neg))