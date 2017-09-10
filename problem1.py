https://projecteuler.net/problem=1
# simplest solution
i = 1
sum = 0
while i < 1000:
    if(i % 3 ==0 or i % 5 == 0):
         sum += i
    i += 1
print(sum)
# 233168

# mathematical solution

i = 999
no_of_multiple_of_3  = i/3
no_of_multiple_of_5  = i/5
no_of_multiple_of_15 = i/15

# formula 1+2+3+ ... +n = (n*(n+1))/2
sum_of_multiple_of_3  = 3 * ((no_of_multiple_of_3 * (no_of_multiple_of_3 + 1)) / 2)
sum_of_multiple_of_5  = 5 * ((no_of_multiple_of_5 * (no_of_multiple_of_5 + 1)) / 2)
sum_of_multiple_of_15 = 15 * ((no_of_multiple_of_15 * (no_of_multiple_of_15 + 1)) / 2)

sum = sum_of_multiple_of_3 + sum_of_multiple_of_5 - sum_of_multiple_of_15
print(sum)
