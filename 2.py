cached_numbers = {} # For memoizing 
sum = 0
term = 1 # Fibonacci numbers starting with 1 & 2

def fib_sum_even(n):
    if n in cached_numbers:
        return cached_numbers[n]
    
    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    else:
        answer = fib_sum_even(n - 1) + fib_sum_even(n - 2)

    cached_numbers[n] = answer
    return answer  

if __name__ == "__main__":
    ''' Calculates sum of even fibonacci numbers such that the terms in fib seq do not exceed 4 million '''
    while(True):
        res = fib_sum_even(term)
        term += 1
        if res > 4000000:
            break
        if res % 2 == 0:
            sum += res

    print(sum)