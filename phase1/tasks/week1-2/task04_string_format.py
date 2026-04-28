"""
任务 4：字符串格式化

任务要求：
1. 使用 f-string 格式化输出个人信息
2. 使用 .format() 方法格式化输出
3. 使用 % 格式化方法
4. 格式化输出浮点数（保留2位小数）
5. 格式化对齐输出（姓名、成绩表格）

知识点：
- f-string: f"{}"
- .format()
- %s, %d, %f
- 对齐：:>10, :<10

难度：⭐⭐
"""

# 数据
name = "小明"
age = 20
score = 95.678
subjects = ["数学", "英语", "Python"]
scores = [95, 88, 92]

# TODO: 1. 使用 f-string 输出：我叫XXX，今年XX岁
print(f'我叫{name}, 今年{age}岁')



# TODO: 2. 使用 .format() 输出相同的内容
print('我叫{}, 今年{}岁'.format(name, age))



# TODO: 3. 使用 % 格式化输出相同的内容
print('我叫%s, 今年%d岁' % (name, age))



# TODO: 4. 输出成绩（保留2位小数）
for s in scores:
    print(f'我的成绩: {s:.2f}')



# TODO: 5. 格式化输出成绩表格（对齐）
# 期望输出：
# 科目    成绩
# 数学    95
# 英语    88
# Python  92
# 在此处写代码
print('科目\t成绩')
for i in range(len(subjects)):
	print(f'{subjects[i]:<8}{scores[i]}')
