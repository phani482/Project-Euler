"""
##Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
'''i=0
total=0
user=int(input('Enter the range to Find the sum of all the multiples of 3 or 5 below: '))
for i in range(0,user):
    if (i%3==0 or i%5==0):
        total += i
print('sum of multiples of 3 and 5 for numbers below'+ str(user) +'are:', int(total))
'''
"""
Problem 2 
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""
a=1
b=2
c=1
print(a,b,sep=',',end=',')
total_even_val=2
for i in range (1,(400-2)):
    c=b+a
    print(str(c),end=',')
    a=b
    b=c
    if c%2==0:
        total_even_val+=c
        continue

print("sum of even-valued terms of fibonacci seq upto 4 million:",total_even_val)
