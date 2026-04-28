"""
任务 7：if-else 条件分支

任务要求：
1. 根据成绩判断等级（A/B/C/D/F）
2. 判断闰年
3. 判断三角形类型
4. 多条件组合判断（and, or, not）
5. 三元运算符

知识点：
- if/elif/else
- 比较运算符：> < == != >= <=
- 逻辑运算符：and, or, not
- 三元运算符：x if condition else y

难度：⭐⭐
"""

# TODO: 1. 根据分数判断等级
# 90-100: A, 80-89: B, 70-79: C, 60-69: D, 0-59: F
score = 85
print(f'score={score} 等级是:', end = " ")
if 90 <= score <= 100:
	print('A')
elif 80 <= score <= 89:
	print('B')
elif 70 <= score <= 79:
	print('C')
elif 60 <= score <= 69:
	print('D')
else:
	print('F')




# TODO: 2. 判断一个年份是否为闰年
# 闰年条件：能被4整除且不能被100整除，或能被400整除
year = 2024
print(f'{year}', end = ' ')
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
	print('闰年')
else:
	print('不是闰年')



# TODO: 3. 判断三角形类型（等边、等腰、普通）
a, b, c = 3, 4, 5
print(f"判断三角类型 a={a}, b={b}, c={c} 是 ", end=" ")
if a == b and b == c and a == c:
	print('等边')
elif a == b or a == c or b == c:
	print('等腰')
else:
	print('普通')



# TODO: 4. 多条件组合判断
# 输入年龄和是否有票，判断是否能看电影
# 条件：年龄>=18 且有票
age = 30
is_tickt = True
print(f"age={age}, is_tickt={is_tickt} ", end=" ")
if age >= 18 and is_tickt:
	print('看电影')
else:
	print('不看电影')


# TODO: 5. 使用三元运算符判断奇偶数
num = 7
print(f'{num} 是', end=" ")
print('偶数' if num % 2 == 0 else '奇数')
