''' Calculates the sum of all the primes below two million '''

import math

sum = 2 # Considering initial sum of 1st prime i.e., 2

def isPrime(num):
    if num % 2 == 0:
        return False
    for i in range(3, round(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

for i in range(3, 2000000, 2):
    if isPrime(i):
        sum += i

print(sum)

