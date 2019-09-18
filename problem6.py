#find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#brute force

accum_x = 0
accum_y = 0


for x in range (1,101,1):
    accum_x += x**2
    accum_y += x

result = accum_y**2 - accum_x

print(result)