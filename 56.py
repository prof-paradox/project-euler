''' Calculates the maximum digit sum of a^b where a, b < 100 '''

sum = None
max_sum = 0

for i in range(91, 100):
    sum = 0
    for num in str(99 ** i):
        sum += int(num)
    if sum > max_sum:
        max_sum = sum

print(max_sum)