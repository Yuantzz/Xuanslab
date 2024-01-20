import re


def check_consecutive_duplicates(string):
    pattern = r'(.)\1+'  # 匹配连续出现的相同字符
    matches = re.findall(pattern, string)

    if matches:
        return 'Y'
    else:
        return 'N'


# 测试
string = input("请输入字符串: ")
result = check_consecutive_duplicates(string)
print(result)