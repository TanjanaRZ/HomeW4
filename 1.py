# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)

import math

b = 0.000001
pi = math.pi

lng = len((str(1 / b)).split(".")[0])-1

res = str(round(pi)) + "."
for i in range(1, lng + 1):
    res = res + str(pi)[i+1]
        
print(res)





