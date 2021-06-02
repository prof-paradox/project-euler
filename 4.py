''' Calculates the maximum palindromic product of 2  3-digit numbers '''

n = 999
max_palin_prod = 1

def isPalindrome(prod):
    return True if str(prod) == str(prod)[::-1] else False

for i in range(n, 100, -1):
    for j in range(i - 1, 100, -1):
        if isPalindrome(i * j) and (i * j) > max_palin_prod:
            max_palin_prod = i * j

print(max_palin_prod)