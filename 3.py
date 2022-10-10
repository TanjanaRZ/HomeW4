# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

numbers = [1, 1, 65, 5, 8, 8, 65, 1]
res = [numbers[0]]
for i in range(1, len(numbers)):
    unic = True
    for j in range(i):
        if numbers[i] == numbers[j]:
            unic = False
    if unic: res.append(numbers[i])


print(res)