"""
任务 4：字符串格式化 - 参考答案
"""

# 数据
name = "小明"
age = 20
score = 95.678
subjects = ["数学", "英语", "Python"]
scores = [95, 88, 92]

# TODO: 1. 使用 f-string 输出：我叫XXX，今年XX岁
print(f"我叫{name}，今年{age}岁")

# TODO: 2. 使用 .format() 方法
print("我叫{}，今年{}岁".format(name, age))

# TODO: 3. 使用 % 格式化
print("我叫%s，今年%d岁" % (name, age))

# TODO: 4. 输出成绩（保留2位小数）
print(f"成绩：{score:.2f}")

# TODO: 5. 格式化输出成绩表格（对齐）
print(f"\n{'科目':<10}{'成绩'}")
for subj, sc in zip(subjects, scores):
    print(f"{subj:<10}{sc}")
