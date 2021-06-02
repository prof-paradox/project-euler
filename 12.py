import math

prev_sum = 0
factors = 0
tri_num = None
term = 1

while(True):
    factors = 1 # Since a number is always a factor of itself 
    tri_num = prev_sum + term

    for i in range(1, tri_num // 2 + 1):
        if tri_num % i == 0:
            factors += 1

    if factors > 5:
        break

    prev_sum = tri_num
    term += 1
    #print(factors)

print(prev_sum)

