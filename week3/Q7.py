x = int(input("输入第一个数字"))
y = int(input("输入第二个数字"))

while 1:
    z = x % y
    if z == 0:
        break
    else:
        x = y
        y = z

print("最大公约数为：", y)
