import math
dec = float(input("请输入一个十进制小数："))
print("0.", end="")
while 1:
    (n, m) = math.modf(dec)
    print(int(m), end="")
    if n == 0:
        break
    dec = n * 2
