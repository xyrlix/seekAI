"""
任务 2：数据类型与变量 - 参考答案
"""

# TODO: 1. 定义以下变量
age = 25
height = 175.5
name = "小明"
is_student = True

# TODO: 2. 使用 type() 打印每个变量的类型
print(f"age 的类型：{type(age)}")
print(f"height 的类型：{type(height)}")
print(f"name 的类型：{type(name)}")
print(f"is_student 的类型：{type(is_student)}")

# TODO: 3. 类型转换
age_float = float(age)
height_int = int(height)
age_str = str(age)
print(f"age 转浮点数：{age_float}")
print(f"height 转整数：{height_int}")
print(f"age 转字符串：{age_str}")

# TODO: 4. 计算：(age * 365) + (height * 100)，输出结果
result = (age * 365) + (height * 100)
print(f"计算结果：{result}")
