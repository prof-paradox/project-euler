'''
Calculates the 10001st prime number
'''

import math

def isPrime(num):
    if num % 2 == 0:
        return False
    for i in range(3, round(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

natural_no = 3
prime_count = 1 # initial count for 2
max_prime = 2

while prime_count <= 10000:
    if(isPrime(natural_no)):
        prime_count += 1
        max_prime = natural_no
    natural_no += 2 # since 2 is the only even prime number

print(max_prime)