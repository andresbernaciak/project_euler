"""Largest palindrome product

Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


def is_palindrome(s):
    reverse = 0
    n = s
    while (n>0):
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    if reverse == s:
        return True
    else:
        return False

max_product = 0
for i in range(999,99,-1):
    if max_product >= 999*i:
        break
    for j in range(999,i-1,-1):
        p = i * j
        if max_product >= p:
            break
        if is_palindrome(p):
            max_product = p
print(max_product)



   
