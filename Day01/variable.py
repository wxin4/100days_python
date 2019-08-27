a = 321
b = 123

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

print("*********************")

c = 12.345
d = 1 + 5j
e = 'hello'
f = True
g = 'h'

print(type(a))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

print("*********************")

flag1 = 3 > 2
flag2 = 3 < 2
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print(flag1)
print(flag2)
print(flag3)
print(flag4)
print(flag5)
print(flag1 is True)
print(flag1 is not True)

print("*********************")

import math
radius = float(input("Please enter the radius: "))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print("perimeter is: {0}".format(perimeter))
print("area is: {0}".format(area))

print("*********************")

# leap year
year = int(input("Please enter the year: "))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)

