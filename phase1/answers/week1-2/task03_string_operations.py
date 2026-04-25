"""
任务 3：字符串操作基础 - 参考答案
"""

# TODO: 1. 定义一个字符串变量，包含你的自我介绍
intro = "你好，我叫小明，我今年20岁，喜欢学习Python编程。"
print(f"自我介绍：{intro}")

# TODO: 2. 输出字符串的长度
print(f"字符串长度：{len(intro)}")

# TODO: 3. 将字符串转为大写和小写，分别输出
print(f"大写：{intro.upper()}")
print(f"小写：{intro.lower()}")

# TODO: 4. 检查字符串中是否包含"学习"或"Python"
print(f"包含'学习'：{'学习' in intro}")
print(f"包含'Python'：{'Python' in intro}")

# TODO: 5. 将字符串中的某个词替换为另一个词
new_intro = intro.replace("小明", "小红")
print(f"替换后：{new_intro}")

# TODO: 6. 将字符串按空格分割，输出分割后的列表
sentence = "Hello World Python Programming"
words = sentence.split()
print(f"分割结果：{words}")
