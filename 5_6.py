# Вводится число, найти его максимальную цифру
chislo = int(input("enter chislo: "))
chislo_str = str(chislo)
max_num = 0
for i in chislo_str:
    if int(i) >= max_num:
        max_num = int(i)
print(max_num)