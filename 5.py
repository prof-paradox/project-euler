# Calculates smallest positive number that is evenly divisible by all of the numbers from 1 to 20
''' Inefficient method - takes about 2.5 mins
---------------------------------------------
min_mult = None
num = 21

while(True):
    for i in range(2, 21):
        if num % i != 0:
            break
    else:
        min_mult = num
    
    if type(min_mult) == int:
        break
    else:
        num += 1

print(min_mult) 
---------------------------------------------
''' 
# Optimized version below
# -------------------------------------------

import math

def isPrime(n):
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

factor_dict = {}
min_mult = 1

for i in range(2, 21):
    factor_ls = []
    stg = f"{i} = "
    if isPrime(i):
        stg += f"{i}^1, "
        factor_ls.append(i)
    else:
        for j in range(2, i // 2 + 1):
            if isPrime(j) and (i % j) == 0:
                temp = i
                exp = 0

                while(temp % j == 0):
                    exp += 1
                    temp /= j
                    factor_ls.append(j)

                stg += f"{j}^{exp}" + ", "

    print(stg[:len(stg)-2])
    print(factor_ls)
    factor_dict[i] = factor_ls

for i in range(2, 21):
    max_pow = 0
    for num in factor_dict:
        factor_count = factor_dict[num].count(i)
        if factor_count > max_pow:
            max_pow = factor_count
    min_mult *= i ** max_pow
        
print(min_mult)
 