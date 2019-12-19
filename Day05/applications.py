# 寻找水仙花数
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

# 翻转正整数
num = int(input("Enter a non-negative number: "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

# 百钱百🐔问题
# 公鸡5元一只，母鸡3元一只，小鸡1元一只
for x in range(5, 101, 5):
    for y in range(3, 101 - x, 3):
        for z in range(1, 101 - x - y):
            if x + y + z == 100 and x // 5 + y // 3 + z == 100:
                print("{0}公鸡{1}母鸡{2}小鸡".format(x // 5,y // 3,z))