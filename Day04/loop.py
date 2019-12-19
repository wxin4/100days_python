# 1 - 100 even number sum
sum = 0
for i in range(2,101,2):
    sum += i
print(sum)

# 9 * 9 table
for i in range(1,10):
    for j in range(1,i+1):
        print("{0} * {1} = {2}".format(i, j, i * j), end = '\t')
    print()

# prime number
from math import sqrt

num = int(input('Enter a non-negative number: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print("{0} is a prime number".format(num))
else:
    print('{0} is not a prime number'.format(num))

# Greatest Common Divisor and Least Common Multiple
x = int(input("Enter x = "))
y = int(input("Enter y = "))
if x > y:
    x,y = y,x
# start from the small number and move down
for factor in range(x,0,-1):
    if x % factor == 0 and y % factor == 0:
        print("{0} and {1} 's gcd is {2}".format(x, y, factor))
        print("{0} and {1} 's lcm is {2}".format(x, y, x * y // factor))
        break

# print stars
'''
*
**
***
****
*****
'''
row = int(input("how many rows? "))
for i in range(row):
    for j in range(i+1):
        print("*", end='')
    print()

'''
    *
   **
  ***
 ****
*****
'''
for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end = '')
        else:
            print("*", end = '')
    print()

'''
    *
   ***
  *****
 *******
*********
'''
for i in range(row):
    for j in range(row - i - 1):
        print(' ', end = '')
    for k in range(2 * i + 1):
        print('*', end = '')
    print()