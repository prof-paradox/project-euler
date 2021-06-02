''' Calculates the 1st Fibonacci term to contain 1000 digits '''

cached_nums = {1:1, 2:1} # Initial terms given in problem 
term = 3

def fib(n):
    if n in cached_nums:
        return cached_nums[n]
    else:
        cached_nums[n] = fib(n-1) + fib(n-2)
        return cached_nums[n]

while True:
    digits = 0
    ans = fib(term)
    digits = len(str(ans))

    if digits == 1000:
        print(term)
        break

    term += 1
    
