# Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.

def isFactor(number):
    res = True
    for i in range(number - 2):
        if number % (number - (i + 1)) == 0:
            res = False
    return res

number = int(input("Введите число:"))
res = []
for i in range(number - 2):
    if number % (i + 2) == 0 and isFactor(i + 2):
        res.append(i + 2)

print(res)

         





