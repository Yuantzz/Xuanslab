score = int(input("请输入成绩："))
if score < 60:
    print("成绩不合格")

elif score >= 60 and score < 74:
    print("成绩合格")

elif score >= 74 and score < 89:
    print("成绩良好")

elif score >= 89 and score <= 100:
    print("成绩优秀")

else:
    print("成绩错误")
