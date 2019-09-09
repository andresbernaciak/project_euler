# projecteuler.net
# problem 3 - 
# =========
# 
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def max_prime_factor(n):
    factors = []
    i = 2
    while n > 1:
        while n % i ==0:
            factors.append(i)
            n /= i
        i += 1
        if i*i > n:
            if n > 1:
                factors.append(n)
                break
    return factors

results = max(max_prime_factor(600851475143))
print(int(results))