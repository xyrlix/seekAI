"""
任务 2：数据类型与变量

任务要求：
1. 定义整数、浮点数、字符串、布尔值变量
2. 使用 type() 查看每个变量的类型
3. 进行类型转换（int↔float↔str）
4. 计算一个简单的数学表达式并输出

知识点：
- int, float, str, bool
- type() 函数
- 类型转换 int(), float(), str()

难度：⭐
"""

# TODO: 1. 定义以下变量
# age（整数）、height（浮点数）、name（字符串）、is_student（布尔值）
# 在此处写代码
age = 30
height = 1.75
name = "MaxM"
is_student = True


# TODO: 2. 使用 type() 打印每个变量的类型
# 在此处写代码
print(type(age))
print(type(height))
print(type(name))
print(type(is_student))


# TODO: 3. 类型转换
# 将 age 转为浮点数，将 height 转为整数，将 age 转为字符串
# 在此处写代码
age_float = float(age)
height_int = int(height)
age_str = str(age)
print(age_float)
print(height_int)
print(age_str)


# TODO: 4. 计算：(age * 365) + (height * 100)，输出结果
# 在此处写代码
result = (age_float * 365) + (height_int * 100)
print(result)
