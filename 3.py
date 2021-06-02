import math

def isPrime(num):
    # if num % 2 == 0:
        # return False
    for i in range(3, round(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    ''' Calculates the largest prime factor of the given number '''
    n = 600851475143
    max_prime_factor = None

    if isPrime(n):
        max_prime_factor = n
    else:
        for i in range(3, round(math.sqrt(n)) + 1, 2):
            if isPrime(i) and n % i == 0:
                max_prime_factor = i

    print(max_prime_factor)


