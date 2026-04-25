"""
任务 3：字符串操作基础

任务要求：
1. 定义一个字符串，统计它的长度
2. 将字符串转为大写和小写
3. 查找字符串中是否包含某个子串
4. 替换字符串中的部分内容
5. 将字符串按空格分割成列表

知识点：
- len() 函数
- .upper() / .lower()
- in 运算符
- .replace()
- .split()

难度：⭐⭐
"""

# TODO: 1. 定义一个字符串变量，包含你的自我介绍
# 在此处写代码
introduction = "我是一个学生，我来自中国，come from China. I am a student. I learn Python."


# TODO: 2. 输出字符串的长度
# 在此处写代码
print(len(introduction))



# TODO: 3. 将字符串转为大写和小写，分别输出
# 在此处写代码
print(introduction.upper())
print(introduction.lower())



# TODO: 4. 检查字符串中是否包含"学习"或"Python"
# 在此处写代码
print("学习" in introduction)
print("Python" in introduction)



# TODO: 5. 将字符串中的某个词替换为另一个词
# 在此处写代码
print(introduction.replace("Python", "学习Python"))


# TODO: 6. 将字符串按空格分割，输出分割后的列表
# 在此处写代码
print(introduction.split())
