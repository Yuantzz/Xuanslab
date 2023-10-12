x = int(input("请输入数字："))
hx = int(x/2)
for i in range(2, hx+1):
	if x % i == 0:
		print("此数字不是质数")
		exit()
print("此数字是质数")
