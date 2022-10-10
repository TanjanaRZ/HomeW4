# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("k="))
kef = [random.randrange(101) for i in range(k + 2)]
res = ""
for i in range(k - 1):
    if kef[k - i] != 0:
        if kef[k - i] == 1:
            res = res + "x^" + str(k - i) + "+"
        else:
            res = res + str(kef[k - i]) + "x^" + str(k - i) + "+"

if kef[k] != 0:
    if kef[k] == 1:
        res = res + "x"
    else:
        res = res + str(kef[k]) + "x+"

if kef[k + 1] != 0:
    res = res + str(kef[k + 1])
res = res + "=0"

f = open('text.txt','w')
f.write(res)