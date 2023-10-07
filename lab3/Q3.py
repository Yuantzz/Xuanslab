import re
number = str(input("input your ID numbers:"))
re1 = re.compile(r'(^\d{15}$)|(^\d{17}([0-9]|X)$)')
result = re1.match(number)

if result:
    print("身份证号合法")

else:
    print("不合法")
