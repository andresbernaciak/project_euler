#projecteuler.net
#
#problem 1
#=========
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.

#answer: 233,168

# using for loop
accum = 0
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        accum += i
print (accum)


# using list comprehension
list_of_multiples = [x for x in range(1,1000) if (x%3==0 or x%5==0)]
print(sum(list_of_multiples))