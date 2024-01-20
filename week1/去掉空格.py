def remove_spaces(input_str):
    return input_str.replace(" ", "")

# 获取用户输入
user_input = input("请输入一个字符串: ")

# 去掉空格并输出结果
result = remove_spaces(user_input)
print("去掉空格后的字符串:", result)
